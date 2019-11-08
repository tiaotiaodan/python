#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class dbException(Exception):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
try:
    raise dbException("数据库连接失败")
except dbException as e:
    print(e)