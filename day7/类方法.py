#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py



class Dog(object):
    name = "我是类变量"
    def __init__(self,name):
        self.name = name

    @classmethod
    def eat(self):
        print("%s is eating..." %self.name)

d = Dog("zhuangsan")
d.eat( )