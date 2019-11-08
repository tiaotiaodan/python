#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import socket

#声明socket类型，同时生成socket连接对象
server = socket.socket()

#绑定要监听的端口
server.bind(("localhost",6969))

#监控
server.listen(5)

print("等待客户端的连接....")
conn,addr = server.accept() #等电话打进来
#conn 就是客户端连过来而在服务器端为其生成的一个连接实例
print("新连接:",conn,addr)

data = conn.recv(10240)
print("recv:", data)
conn.send(data.upper())

server.close()
