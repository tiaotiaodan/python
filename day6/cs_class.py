#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class Dog(object):
    print("hello,I am a dog!")


d = Dog()  # 实例化这个类，
# 此时的d就是类Dog的实例化对象

# 实例化，其实就是以Dog类为模版，在内存里开辟一块空间，存上数据，赋值成一个变量名


class Dog(object):

    def __init__(self, name, dog_type):
        self.name = name
        self.type = dog_type

    def sayhi(self):
        print("hello,I am a dog, my name is ", self.name)


d = Dog('LiChuang', "京巴")
d.sayhi()