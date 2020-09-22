#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

# Echo server program
import socket

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 8000  # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # 1参数：常量表示地址和协议簇，第2个参数表示套接字类型
    s.bind((HOST, PORT))
    s.listen(1)  # 监听端口并设置最大连接数
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)

# https://docs.python.org/zh-cn/3.7/library/socket.html


"""
一台服务器，它将收到的所有数据原样返回（仅服务于一个客户端），还有一个使用该服务器的客户端。
注意，服务器必须按序执行 socket(), bind(), listen(), accept() （可能需要重复执行 accept() 以服务多个客户端），
而客户端仅需要按序执行 socket(), connect()。还须注意，服务器不在侦听套接字上发送 sendall()/recv()，
而是在 accept() 返回的新套接字上发送。
"""
