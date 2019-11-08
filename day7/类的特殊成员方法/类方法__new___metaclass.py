#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


#特殊案例
def func(self):
    print("hell word! %s" %self.name)


def __init__(self,name,age):
    self.name = name
    self.age = age
foo = type('foo',(object,),{'func': func,'__init__':__init__})

f = foo("zhangsan",22)
f.func()
print(type(foo))

#普通案例
class foo(object):
    def func(self):
        print("hello word!")


f = foo( )
print(f)


#案例class使用方式
class Foo(object):
    def __init__(self,name):
        self.name = name

f = Foo("alex")

print(type(f))
print(type(Foo))




