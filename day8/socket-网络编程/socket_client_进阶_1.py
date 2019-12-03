#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  socket

client = socket.socket()

client.connect(("127.0.0.1",8001))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))

    data = client.recv(10240)
    print("来自服务器",data)


client.close()