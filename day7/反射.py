#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

def bulk(self):
    print("%s is yelling..." %self.name)

class Foo(object):
    def __init__(self,name):
        self.name = name

    def func(self,food):
        print("%s is func..."%self.name,food)

f =  Foo("zhangsan")
choice = input(">>:").strip()


# print(hasattr(f,choice))      ## hasattr 判断一个obj对象里是否有对象的name_str字符串的方法 ###
# print(getattr(f,choice))      ##getattr 根据字符串去获取obj对象里的对应的方法的内存地址 ###
#
# getattr(f,choice) ()          ## getattr 调用程序 ##

if hasattr(f,choice):
    d = getattr(f,choice)
    d("aa")
else:
    setattr(f,choice,bulk)    #setattr 通过配置修改名称
    f.talk(f)

if hasattr(f,choice):
    delattr(f,choice)       #delattr 删除成员