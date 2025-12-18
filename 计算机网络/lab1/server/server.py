#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Web服务器主程序
功能：基于Socket的HTTP服务器，可配置化部署，支持静态文件和动态请求处理
作者：根据用户需求实现
版本：1.0
"""

import socket
import sys
import os
from datetime import datetime
from configparser import ConfigParser
from request_handler import RequestHandler


class WebServer:
    """
    Web服务器类
    
    功能：实现一个简单的HTTP服务器，支持配置化部署和请求日志记录
    特性：
    - 可配置监听地址、端口和主目录
    - 单线程处理请求
    - 详细的请求日志记录
    - 异常处理和错误提示
    """
    
    def __init__(self, config_file='config.ini'):
        """
        初始化Web服务器，读取配置文件
        
        参数:
            config_file: 配置文件路径，默认为config.ini
        """
        # 读取配置文件
        self.config = ConfigParser()
        self.config.read(config_file)

        host = input('请输入服务器IP地址：')
        port = int(input('请输入端口号：'))
        document_root = input('请输入主目录：')
        
        # 读取服务器配置参数，使用fallback值确保兼容性
        self.host = host if host else self.config.get('server', 'host', fallback='127.0.0.1')
        self.port = int(port) if port else self.config.getint('server', 'port', fallback=8080)
        self.document_root = document_root if document_root else self.config.get('server', 'document_root', fallback='./www')
        self.log_requests = self.config.getboolean('logging', 'log_requests', fallback=True)
        self.log_responses = self.config.getboolean('logging', 'log_responses', fallback=True)
        
        # 确保主目录存在，如果不存在则创建
        if not os.path.exists(self.document_root):
            os.makedirs(self.document_root)
            print(f"创建主目录: {self.document_root}")
        
        # 创建请求处理器实例，用于处理HTTP请求
        self.handler = RequestHandler(self.document_root)
        
        # 创建服务器socket并设置端口复用[1](@ref)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    def start(self):
        """
        启动Web服务器主循环
        
        功能：
        - 绑定地址和端口
        - 开始监听连接
        - 处理客户端请求
        - 异常处理和资源清理
        """
        try:
            # 绑定服务器地址和端口
            self.server_socket.bind((self.host, self.port))
            # 开始监听，设置等待连接队列长度为5
            self.server_socket.listen(5)
            
            # 输出服务器启动信息
            print(f"Web服务器已启动在 http://{self.host}:{self.port}")
            print(f"主目录: {os.path.abspath(self.document_root)}")
            print("请求日志已启用")
            print("按 Ctrl+C 停止服务器\n")
            
            # 主服务循环
            while True:
                try:
                    # 等待客户端连接，accept()会阻塞直到有连接到来
                    client_socket, client_address = self.server_socket.accept()
                    
                    # 处理客户端请求
                    self._handle_client(client_socket, client_address)
                    
                except KeyboardInterrupt:
                    # 捕获Ctrl+C信号，优雅关闭服务器
                    print("\n服务器正在关闭...")
                    break
                except Exception as e:
                    # 捕获其他异常，防止服务器崩溃
                    print(f"处理客户端连接时出错: {e}")
                    
        except Exception as e:
            # 服务器启动失败的异常处理
            print(f"服务器启动失败: {e}")
        finally:
            # 确保服务器socket被关闭，释放资源
            self.server_socket.close()
    
    def _handle_client(self, client_socket, client_address):
        """
        处理单个客户端连接
        
        参数:
            client_socket: 客户端socket对象
            client_address: 客户端地址信息(IP,端口)
        
        处理流程：
        1. 接收HTTP请求数据
        2. 记录请求日志
        3. 处理请求并生成响应
        4. 发送响应并记录结果
        5. 异常处理和资源清理
        """
        try:
            # 接收客户端发送的HTTP请求数据，最大接收4096字节[2](@ref)
            request_data = client_socket.recv(4096).decode('utf-8')
            
            # 如果接收数据为空，直接返回
            if not request_data:
                return
            
            # 记录请求日志
            if self.log_requests:
                self._log_event('REQUEST', client_address, request_data)
            
            # 调用请求处理器处理HTTP请求，获取响应数据和文件路径
            response_data, file_path = self.handler.handle_request(request_data)
            
            # 发送响应数据给客户端
            client_socket.sendall(response_data)
            
            # 记录响应日志
            if self.log_responses:
                self._log_event('RESPONSE', client_address, file_path=file_path)
                
        except Exception as e:
            # 生成500错误响应并发送给客户端
            error_msg = f"HTTP/1.1 500 Internal Server Error\r\n\r\n500 Error: {str(e)}"
            client_socket.send(error_msg.encode())
            # 记录错误日志
            self._log_event('ERROR', client_address, error_message=str(e))
        finally:
            # 确保客户端socket被关闭
            client_socket.close()
    
    def _log_event(self, event_type, client_address, request_data=None, file_path=None, error_message=None):
        """
        统一日志记录函数 - 合并原来的_log_request和_log_response功能
        
        参数:
            event_type: 事件类型 ('REQUEST', 'RESPONSE', 'ERROR')
            client_address: 客户端地址(IP,端口)
            request_data: 请求数据(仅REQUEST类型需要)
            file_path: 文件路径(仅RESPONSE类型需要)
            error_message: 错误信息(仅ERROR类型需要)
        
        功能：根据事件类型生成格式化的日志输出，避免变量作用域问题[6,7](@ref)
        """
        client_ip, client_port = client_address
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 统一的日志格式框架
        print("┌" + "─" * 70 + "┐")
        print(f"│ 事件类型: {event_type} | 时间: {timestamp}")
        print("├" + "─" * 70 + "┤")
        print(f"│ ▪ 客户端地址: {client_ip}:{client_port}")
        
        # 根据事件类型输出不同的详细信息
        if event_type == 'REQUEST' and request_data:
            # 解析HTTP请求行[1](@ref)
            lines = request_data.split('\r\n')
            request_line = lines[0] if lines else "Unknown Request"
            print(f"│ ▪ HTTP请求行: {request_line}")
            
            # 显示简化的请求头信息（前几个头部）
            if len(lines) > 1:
                # 过滤掉常见的自动生成的头部，显示有意义的头部
                meaningful_headers = [line for line in lines[1:5] if line and not line.startswith(('Accept', 'Connection', 'Cache-Control'))]
                if meaningful_headers:
                    print(f"│ ▪ 请求头部样本:")
                    for header in meaningful_headers[:2]:  # 只显示前两个有意义的头部
                        header_display = header[:50] + "..." if len(header) > 50 else header
                        print(f"│   {header_display}")
        
        elif event_type == 'RESPONSE':
            if file_path and os.path.exists(file_path):
                # 成功响应日志
                try:
                    file_size = os.path.getsize(file_path)
                    file_name = os.path.basename(file_path)
                    
                    # 根据文件扩展名判断文件类型[5](@ref)
                    file_ext = os.path.splitext(file_name)[1].lower()
                    file_type = "文本" if file_ext in ['.html', '.css', '.js', '.txt', '.xml'] else \
                            "图片" if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'] else \
                            "媒体" if file_ext in ['.mp4', '.mp3', '.avi', '.mov'] else \
                            "文件"
                    
                    print(f"│ ▪ 响应状态: 成功")
                    print(f"│ ▪ 文件类型: {file_type}")
                    print(f"│ ▪ 文件名称: {file_name}")
                    print(f"│ ▪ 文件大小: {file_size} bytes")
                except OSError as e:
                    print(f"│ ▪ 响应状态: 成功（但无法获取文件详情）")
                    print(f"│ ▪ 错误详情: 文件访问错误 - {str(e)}")
            else:
                # 错误响应日志
                print(f"│ ▪ 响应状态: 失败")
                if file_path is None:
                    print(f"│ ▪ 错误原因: 非法路径请求（路径安全检查失败）")
                elif not os.path.exists(file_path):
                    file_name = os.path.basename(file_path) if file_path else "未知文件"
                    print(f"│ ▪ 错误原因: 文件未找到 - {file_name}")
                    print(f"│ ▪ 建议操作: 检查文件路径是否正确或文件是否存在")
                else:
                    print(f"│ ▪ 错误原因: 文件访问权限不足")
                    print(f"│ ▪ 建议操作: 检查文件权限设置")
        
        elif event_type == 'ERROR' and error_message:
            # 错误事件日志
            print(f"│ ▪ 错误类型: 服务器内部错误")
            print(f"│ ▪ 错误信息: {error_message}")
            print(f"│ ▪ 处理建议: 检查服务器日志或联系管理员")
        
        # 公共的日志结束部分
        print("└" + "─" * 70 + "┘")
        print()  # 空行分隔日志条目


def main():
    """
    主函数 - 程序入口点
    
    功能：
    - 处理命令行参数
    - 创建默认配置文件(如果需要)
    - 启动Web服务器
    """
    # 处理配置文件参数，支持命令行指定配置文件
    config_file = 'config.ini'
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    
    # 如果配置文件不存在，创建默认配置[2](@ref)
    if not os.path.exists(config_file):
        print(f"配置文件 {config_file} 不存在，使用默认配置")
        # 这里可以添加创建默认配置文件的代码
    
    # 创建并启动Web服务器实例
    server = WebServer(config_file)
    server.start()


# Python标准的主程序入口点[3](@ref)
if __name__ == '__main__':
    main()