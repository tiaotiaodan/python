#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  socket
client = socket.socket()

client.connect(("127.0.0.1",8888))

while True:
    msg = input("请你输出:").strip()
    if len(msg) == 0:continue
    client.send( msg.encode("utf-8"))

    data = client.recv(10240)
    print(data.decode())

client.close()