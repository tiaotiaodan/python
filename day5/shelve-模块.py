#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import shelve
import datetime

#以下是创建文件，存储数据
d = shelve.open('shelve_test')  # 打开一个文件

info = { 'age':22,"job":'it'}

name = ["alex", "rain", "test"]
d["test"] = name  # 持久化列表
d["info"] = info  # 持久化类
d["date"] = datetime.datetime.now()

d.close()


#以下是打开配置文件，读取文件数据
d = shelve.open('shelve_test')  # 打开一个文件
print(d.get("test"))
print(d.get("info"))
print(d.get("date"))









