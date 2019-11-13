#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import paramiko

trabsport = paramiko.Transport(('192.168.200.130', 22))
trabsport.connect(username='root',password='123456')

sftp = paramiko.SFTPClient.from_transport(trabsport)
sftp.put('a.html','/tmp/a.html')


trabsport.close()