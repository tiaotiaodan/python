#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class Foo:

    def __init__(self,name):
        self.name = name
        print("初始化！__init方法 %s "  % self.name)

    def __call__(self, *args, **kwargs):
        print("打印__call__",args,kwargs)

b = Foo("zhangsan")
b(1,2,3,cc=444)