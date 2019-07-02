#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import getpass


UserName = 'shichao'
PassWord = 'abc123'
username = input("username:")
password = input("password:")

if UserName == username  and PassWord == password:
    print("Welcome user {name} login..." .format(name=username))
else:
    print("invalid username or password")
