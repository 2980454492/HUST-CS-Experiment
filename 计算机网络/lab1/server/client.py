import socket
from urllib.parse import urlparse

def test_web_server():
    """测试Web服务器的客户端程序"""
    # 连接服务器
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        host = input('请输入想要连接的服务器IP地址：')
        port = int(input('请输入想要连接的服务器端口号：'))

        client_socket.connect((host, port))
        print('已连接服务器！')
        
        while True:
            # 获取用户输入
            user_input = input('\n请输入URL (或输入 "bye" 退出): ').strip()
            
            if user_input.lower() == 'bye':
                # 发送退出消息
                client_socket.send(b'bye')
                break
            
            if not user_input:
                continue
            
            # 解析URL并构建HTTP请求[6](@ref)
            try:
                if user_input.startswith('http://'):
                    # 解析URL
                    parsed_url = urlparse(user_input)
                    path = parsed_url.path if parsed_url.path else '/index.html'
                    host = parsed_url.netloc
                    
                    # 构建标准HTTP GET请求[7](@ref)
                    http_request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
                else:
                    # 直接发送原始URL字符串（服务器会解析）
                    http_request = user_input + '\r\n\r\n'
                
                # 发送请求
                client_socket.send(http_request.encode('utf-8'))
                print(f"已发送请求: {user_input}")
                
                # 接收响应
                response = b""
                while True:
                    data = client_socket.recv(4096)  # 增加缓冲区以适应大文件
                    if not data:
                        break
                    response += data
                    # 简单判断是否接收完整（对于大文件可能需要更复杂的逻辑）
                    if len(data) < 4096:
                        break
                
                # 解析HTTP响应
                response_str = response.decode('utf-8', errors='ignore')
                header_end = response_str.find('\r\n\r\n')
                
                if header_end != -1:
                    headers = response_str[:header_end]
                    body = response_str[header_end+4:]
                    
                    print("服务器响应头:")
                    print(headers)
                    
                    # 检查Content-Type
                    if 'image/' in headers:
                        print("接收到图片数据（二进制内容已省略显示）")
                    else:
                        print("响应内容:")
                        print(body[:500] + "..." if len(body) > 500 else body)
                else:
                    print("完整响应:")
                    print(response_str[:1000] + "..." if len(response_str) > 1000 else response_str)
                    
            except Exception as e:
                print(f"处理请求时出错: {e}")
                
    except ConnectionRefusedError:
        print("无法连接到服务器，请确保服务器已启动")
    except Exception as e:
        print(f"连接错误: {e}")
    finally:
        client_socket.close()
        print("连接已关闭")

if __name__ == '__main__':
    print("Web服务器测试客户端")
    print("=" * 50)
    test_web_server()