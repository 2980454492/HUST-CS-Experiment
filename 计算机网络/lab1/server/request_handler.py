import os
import mimetypes
from datetime import datetime
from urllib.parse import unquote

class RequestHandler:
    def __init__(self, document_root):
        self.document_root = os.path.abspath(document_root)
        # 初始化MIME类型映射
        mimetypes.add_type('text/html', '.html')
        mimetypes.add_type('text/css', '.css')
        mimetypes.add_type('application/javascript', '.js')
        mimetypes.add_type('image/jpeg', '.jpg')
        mimetypes.add_type('image/jpeg', '.jpeg')
        mimetypes.add_type('image/png', '.png')
        mimetypes.add_type('image/gif', '.gif')
        mimetypes.add_type('image/webp', '.webp')
        mimetypes.add_type('image/svg+xml', '.svg')
    
    def handle_request(self, request_data):
        """处理HTTP请求并返回响应数据及文件路径"""
        try:
            # 解析请求行
            lines = request_data.split('\r\n')
            if not lines:
                return self._create_error_response(400, "Bad Request - 请求格式错误"), None
            
            request_line = lines[0]
            parts = request_line.split()
            
            if len(parts) < 2:
                return self._create_error_response(400, "Bad Request - 请求行格式不正确"), None
            
            method, path = parts[0], parts[1]
            
            # 只支持GET方法[6](@ref)
            if method != 'GET':
                return self._create_error_response(405, "Method Not Allowed - 仅支持GET方法"), None
            
            # 解码URL编码的路径
            path = unquote(path)
            
            # 构建安全的文件路径
            file_path = self._get_safe_path(path)
            
            if file_path is None:
                return self._create_error_response(403, "Forbidden - 路径访问被拒绝"), None
            
            # 检查文件是否存在[1,2](@ref)
            if not os.path.exists(file_path):
                return self._create_error_response(404, f"Not Found - 文件不存在: {os.path.basename(file_path)}"), file_path
            
            # 检查是否是文件（不是目录）
            if not os.path.isfile(file_path):
                return self._create_error_response(404, "Not Found - 请求的资源不是文件"), file_path
            
            # 检查文件权限[1,5](@ref)
            if not os.access(file_path, os.R_OK):
                return self._create_error_response(403, "Forbidden - 文件读取权限不足"), file_path
            
            # 获取MIME类型
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            
            # 读取文件内容（区分文本和二进制文件）
            try:
                if mime_type.startswith('text/'):
                    # 文本文件使用文本模式读取
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read().encode('utf-8')
                else:
                    # 二进制文件（图片等）使用二进制模式读取
                    with open(file_path, 'rb') as f:
                        file_content = f.read()
            except PermissionError:
                return self._create_error_response(403, "Forbidden - 文件访问被拒绝"), file_path
            except UnicodeDecodeError:
                return self._create_error_response(500, "Internal Server Error - 文件编码错误"), file_path
            except Exception as e:
                return self._create_error_response(500, f"Internal Server Error - 文件读取失败: {str(e)}"), file_path
            
            # 构建成功的HTTP响应
            response_headers = [
                f"HTTP/1.1 200 OK",
                f"Content-Type: {mime_type}",
                f"Content-Length: {len(file_content)}",
                f"Connection: close",
                f"Date: {datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}",
                f"Server: PythonWebServer/1.0",
                f"\r\n"
            ]
            
            response_header = '\r\n'.join(response_headers)
            response_data = response_header.encode('utf-8') + file_content
            
            return response_data, file_path
            
        except Exception as e:
            # 捕获所有未预期的异常
            return self._create_error_response(500, f"Internal Server Error - 服务器内部错误: {str(e)}"), None
    
    def _get_safe_path(self, path):
        """安全地构建文件路径，防止目录遍历攻击[1](@ref)"""
        # 处理根路径请求
        if path == '/':
            path = '/index.html'
        
        # 移除查询参数和片段标识
        path = path.split('?')[0].split('#')[0]
        
        # 构建绝对路径
        absolute_path = os.path.abspath(os.path.join(self.document_root, path.lstrip('/')))
        
        # 安全检查：确保请求的路径在文档根目录内
        if not absolute_path.startswith(self.document_root):
            return None
        
        return absolute_path
    
    def _create_error_response(self, status_code, status_message):
        """创建详细的错误响应页面"""
        # 根据状态码生成不同的错误信息
        error_info = {
            400: {"title": "400 Bad Request", "description": "请求格式不正确，服务器无法理解。"},
            403: {"title": "403 Forbidden", "description": "您没有权限访问此资源。"},
            404: {"title": "404 Not Found", "description": "请求的资源不存在，请检查URL是否正确。"},
            405: {"title": "405 Method Not Allowed", "description": "请求方法不被允许。"},
            500: {"title": "500 Internal Server Error", "description": "服务器内部错误，请稍后重试。"}
        }
        
        info = error_info.get(status_code, {"title": f"{status_code} Error", "description": status_message})
        
        error_html = f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{info['title']}</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: #333;
                }}
                .error-container {{
                    background: rgba(255, 255, 255, 0.95);
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
                    max-width: 600px;
                    width: 90%;
                    text-align: center;
                }}
                .error-icon {{
                    font-size: 4em;
                    margin-bottom: 20px;
                }}
                .error-title {{
                    color: #d32f2f;
                    font-size: 2.5em;
                    margin-bottom: 15px;
                    font-weight: 300;
                }}
                .error-description {{
                    font-size: 1.2em;
                    margin-bottom: 25px;
                    line-height: 1.6;
                    color: #555;
                }}
                .error-details {{
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 8px;
                    margin: 20px 0;
                    text-align: left;
                    font-family: 'Courier New', monospace;
                    font-size: 0.9em;
                }}
                .home-button {{
                    display: inline-block;
                    background: #667eea;
                    color: white;
                    padding: 12px 30px;
                    text-decoration: none;
                    border-radius: 5px;
                    transition: all 0.3s ease;
                    font-size: 1.1em;
                    margin-top: 10px;
                }}
                .home-button:hover {{
                    background: #5a6fd8;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                }}
                .server-info {{
                    margin-top: 20px;
                    font-size: 0.9em;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <div class="error-icon">
                    {'❌' if status_code >= 500 else '⚠️' if status_code >= 400 else 'ℹ️'}
                </div>
                <h1 class="error-title">{info['title']}</h1>
                <p class="error-description">{info['description']}</p>
                
                <div class="error-details">
                    <strong>详细错误信息:</strong><br>
                    {status_message}
                </div>
                
                <a href="/" class="home-button">返回首页</a>
                
                <div class="server-info">
                    <p>服务器时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    <p>Python Web Server 1.0</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        response_headers = [
            f"HTTP/1.1 {status_code} {info['title']}",
            "Content-Type: text/html; charset=utf-8",
            f"Content-Length: {len(error_html.encode('utf-8'))}",
            "Connection: close",
            "\r\n"
        ]
        
        response_header = '\r\n'.join(response_headers)
        return (response_header + error_html).encode('utf-8')