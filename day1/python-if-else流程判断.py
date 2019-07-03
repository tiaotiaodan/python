#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
'''

 提示输入用户名和密码
 验证用户名和密码
 如果错误，则输出用户名或密码错误
 如果成功，则输出 欢迎，XXX!

'''

import getpass

UserName = 'shichao'
PassWord = 'abc123'
username = input("请你输入用户名：")
password = input("请你输入密码：")

if UserName == username  and  PassWord == password:
    print("输入正确，欢迎进入")
else:
    print("输入用户名或密码错误")