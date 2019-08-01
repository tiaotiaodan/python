#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

name = "zhangsan"

def  change_name(name):
    print("before change:", name)
    name = "李四有一辆宝马汽车"
    print("after change:",name)

change_name(name)
print("在外面看看name改变了没？", name)