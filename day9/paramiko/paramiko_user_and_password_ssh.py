#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  paramiko

#创建ssh对象
ssh = paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接服务器
ssh.connect(hostname='192.168.200.130',port=22,username='root',password='123456')

#执行命令 stdout：为正确输出，stderr为错误输出，同时是有一个变量有值
stdin, stdout, stderr = ssh.exec_command('df')

result  =  stdout.read().decode('utf-8')

print(result)


#关闭连接
ssh.close()
