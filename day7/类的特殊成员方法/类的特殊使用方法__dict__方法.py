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


#打印类里的所有属性，不包括实例属性
print(Foo.__dict__)

#通过实例调用，打印所有实例属性，不包括类属性
d = Foo("zhangsan")
print(d.__dict__)

