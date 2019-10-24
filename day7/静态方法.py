#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


class Dog(object):


    def __init__(self,name):
        self.name = name

    @staticmethod     #实际上跟类没什么关系了
    def eat(self):
        print("%s is eating %s "  %(self.name,'馒头'))



d = Dog("zhangsan")
d.eat(d)


