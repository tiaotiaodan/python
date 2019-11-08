#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


try:
    raise Exception("数据库连接被拒绝...")
except Exception as e:
    print(e)
