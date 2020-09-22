#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

import socket


def handle_request(clint):
    buf = clint.recv(1024)
    clint.send(bytes("HTTP/1.1 200 OK\r\n\r\n".encode('utf_8')))
    clint.send(bytes("hello word".encode('utf_8')))


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 1参数：常量表示地址和协议簇，第2个参数表示套接字类型
    sock.bind(('localhost', 8000))
    sock.listen(5)  # 监听端口并设置最大连接数

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()

"""
socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
使用给定的地址簇、套接字类型和协议号创建一个新的套接字。地址簇应为 AF_INET （默认）、
AF_INET6、AF_UNIX、AF_CAN、AF_PACKET 或 AF_RDS 其中之一。套接字类型应为 SOCK_STREAM （默认）、
SOCK_DGRAM、SOCK_RAW 或其他 SOCK_ 常量之一。协议号通常为零，可以省略，或者在地址簇为 AF_CAN 的情况下，
协议号应为 CAN_RAW、CAN_BCM 或 CAN_ISOTP 之一。

如果指定了 fileno，那么将从这一指定的文件描述符中自动检测 family、type 和 proto 的值。
如果调用本函数时显式指定了 family、type 或 proto 参数，可以覆盖自动检测的值。
这只会影响 Python 表示诸如 socket.getpeername() 一类函数的返回值的方式，而不影响实际的操作系统资源。
与 socket.fromfd() 不同，fileno 将返回原先的套接字，而不是复制出新的套接字。
这有助于在分离的套接字上调用 socket.close() 来关闭它。
"""


import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)


# Echo client program
import socket

HOST = 'daring.cwi.nl'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))