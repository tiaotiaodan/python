#_*_coding:utf-8_*_
__author__ = 'Alex Li'


import socket
import os,subprocess


server = socket.socket() #获得socket实例
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("localhost",9999)) #绑定ip port
server.listen()  #开始监听

while True: #第一层loop
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:

        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break #这里断开就会再次回到第一次外层的loop
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read() #py3 里socket发送的只有bytes,os.popen又只能接受str,所以要decode一下

        print("before send",len(cmd_res))
        if len(cmd_res) == 0:
            res = "cmd exec success,has not output!".encode("utf-8")
        conn.send(str(len(cmd_res.encode())).encode("utf-8")) #发送数据之前,先告诉客户端要发多少数据给它
        conn.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()

