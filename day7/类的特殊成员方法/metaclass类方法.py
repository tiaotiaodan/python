#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


class MyType(type):
    def __init__(self,*args,**kwargs):
        print("Mytype __init__",*args,**kwargs)

    def __call__(self, *args, **kwargs):
        print("Mytype __call__", *args, **kwargs)
        obj = self.__new__(self)
        print("obj ",obj,*args, **kwargs)
        print(self)
        self.__init__(obj,*args, **kwargs)
        return obj

    def __new__(cls, *args, **kwargs):
        print("Mytype __new__",*args,**kwargs)
        return type.__new__(cls, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType

    def __init__(self,name):
        self.name = name
        print("Foo __init__")

    def __new__(cls, *args, **kwargs):
        print("Foo __new__")
        return object.__new__(cls)       #继承父亲的__new__方法

f = Foo("张三")
print(f.name)




