#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

#面向过程
def func1():
    print("in the func1")
    return 0
def func2():
    print("in the func2")

x=func1()
y=func2()

print("from func1 return is %s" %x)
print("from func2 return is %s" %y)