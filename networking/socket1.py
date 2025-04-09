import socket
import select
import sys
from rich.logging import RichHandler
import logging
from rich.traceback import install
from rich import print as rprint

# 初始化 rich 的错误追踪
install()

from rich import pretty
pretty.install()

# 配置 logging 使用 RichHandler（但不解析消息中的 markup）
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler(
        rich_tracebacks=True,
        show_time=True,
        show_level=True
    )]
)
logger = logging.getLogger("SocketServer ")

def log_with_style(message, style=""):
    """通过 rich.print 输出带样式的消息，同时用 logging 记录原始消息"""
    rprint(f"[{style}]{message}[/{style}]")
    logger.info(message)

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setblocking(False)
    server_socket.bind(('127.0.0.1', 8020))
    server_socket.listen(5)
    log_with_style("Server is listening on 127.0.0.1:8020", "bold green")

    inputs = [server_socket]
    outputs = []

    while True:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server_socket:
                try:
                    client_socket, client_address = s.accept()
                    log_with_style(f"New connection from {client_address}", "cyan")
                    client_socket.setblocking(False)
                    inputs.append(client_socket)
                except Exception as e:
                    logger.error(f"Accept error: {e}")
            else:
                try:
                    data = s.recv(1024)
                    if data:
                        decoded = data.decode()
                        # 分开打印接收的数据和客户端信息
                        rprint(f"[yellow]Received: {decoded}[/yellow]")
                        rprint(f"[magenta]From: {s.getpeername()}[/magenta]")
                        logger.info(f"Received: {decoded} from {s.getpeername()}")

                        if s not in outputs:
                            outputs.append(s)
                    else:
                        log_with_style(f"Closing connection to {s.getpeername()}", "orange3")
                        inputs.remove(s)
                        s.close()
                except ConnectionResetError:
                    logger.error(f"Connection reset by peer: {s.getpeername()}")
                    inputs.remove(s)
                    s.close()
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")
                    inputs.remove(s)
                    s.close()

        for s in writable:
            try:
                s.send(b"Message received\n")
                outputs.remove(s)
            except Exception as e:
                logger.error(f"Send error: {e}")
                outputs.remove(s)

        for s in exceptional:
            logger.error(f"Exceptional condition for {s.getpeername()}")
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()

except KeyboardInterrupt:
    log_with_style("\nServer shutting down.", "bold green")
except Exception as e:
    logger.critical(f"Fatal error: {e}", exc_info=True)
finally:
    server_socket.close()
    log_with_style("Server socket closed", "bold green")