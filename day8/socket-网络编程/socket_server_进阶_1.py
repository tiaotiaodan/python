#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import socket

server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen(5)

print("等待client端请求...")

conn,addr = server.accept()
print("新连接:",addr)

while True:
    data = conn.recv(10240)
    if not data:
        print("客户端断开了...")
        break
    print("收到消息:",data)
    conn.send(data.upper())

server.close()

