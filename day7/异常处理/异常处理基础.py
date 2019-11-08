#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

s1 = 'hello'
try:
    int(s1)
except ValueError as  e:
    print(e)


dic = { "wupeiqi": "alex" }
try:
    dic['k10']
except KeyError as e:
    print(e)




dic = ["wupeiqi", 'alex']
try:
    dic[10]
except IndexError as e:
    print(e)





# while True:
#     num1 = input("num1:")
#     num2 = input("num2:")
#     try:
#         num1 = int(num1)
#         num2 = num2(num2)
#         result = num1 + num2
#     except Exception as e:
#         print("出现异常，信息如下：")
#         print(e)