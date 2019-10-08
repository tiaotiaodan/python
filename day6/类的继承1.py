#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class People:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating...." % self.name)

    def talk(self):
        print("%s is sleep.." % self.name)

    def sleep(self):
        print("%s is sleep.." % self.name)


class Man(People):     #子类
    def __init__(self,name,age,money):
        People.__init__(self,name,age)
        self.money = money
        print("%s 一出生就有 money.." % self.name )

    def piao(self):
        print("%s is piaoing...."   % self.name)

    def sleep(self):                   #重构了父类的方法。
        People.sleep(self)              #调用父类方法
        print("man is sleeping...")


class Woman(People):
    def get_birth(self):
        print("%s is born get_birth" % self.name)


m1 = Man("zhangsan",22,10)

m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("chenRonghua",26)
w1.get_birth()