#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' % self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)


def func(obj):
    obj.talk()

c1 = Cat("小猫")
d1 = Dog("小狗")

func(c1)
func(d1)