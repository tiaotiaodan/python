#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(("localhost",6969))
client.send(b"hello world!")

data = client.recv(10240)

print("recv:",data)

client.close()
