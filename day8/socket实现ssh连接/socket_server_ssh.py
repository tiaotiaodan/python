#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import socket
import os

server = socket.socket()    #获取socket实例
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


server.bind(("localhost",8888))   #绑定IP port
server.listen(5)  #开始监听

while True:
    print("等待客户端的连接...")
    conn,addr = server.accept()   #接受并建立与客户端的连接，程序在此处开始阻塞，只到有客户端连接进来....
    print("新连接",addr)

    while True:
        data = conn.recv(10240)
        if not data:
            print("客户端断开了....")
            break   #这里断开就会再次回到第一次外层的loop
        print("收到命令",data)
        res = os.popen(data.decode()).read()
        print(len(res))
        conn.send(res.encode("utf-8"))

server.close()