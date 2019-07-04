#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

age = 25

count = 0
while True:
    if  count == 3:
        break
    user_age = int(input("请输入才猜年龄数字："))
    if user_age == age :
        print("猜年龄正确")
        break
    elif user_age < age :
        print("你才的年龄数字小于正确年龄")
    elif user_age > age :
        print("你才的年龄数字大于正确年龄")
    count = count + 1

