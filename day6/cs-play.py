#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name = name   #实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):                    #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name))


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist','B22')  #生成一个角色

r1.buy_gun("AK47")