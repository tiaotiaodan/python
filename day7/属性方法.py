#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


class Dog(object):
    def __init__(self,name):
        self.name = name

    @property
    def eat(self):
        print("%s is eating" % self.name)

d = Dog("zhangsan")
d.eat