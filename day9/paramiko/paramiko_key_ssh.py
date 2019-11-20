#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import paramiko

key_ssh = paramiko.RSAKey.from_private_key_file('c:/Users/qq111/Desktop/id_rsa')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.200.142',port=22,username='root', pkey=key_ssh)

stdin, stdout, stderr = ssh.exec_command('df')

result  = stdout.read().decode('utf-8')

print(result)

ssh.close()