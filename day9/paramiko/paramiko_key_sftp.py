#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import paramiko

key_ssh = paramiko.RSAKey.from_private_key_file('c:/Users/qq111/Desktop/id_rsa')

tran = paramiko.Transport(('192.168.200.142', 22))
tran.connect(username='root',pkey=key_ssh)

sftp = paramiko.SFTPClient.from_transport(tran)

#将b.html  上传至服务器 /tmp/b.html
sftp.put('b.html','/tmp/b.html')


tran.close()


