#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

s1 = '1223'
try:
    int(s1)
except Exception as e:
    print(e)

else:
    print("当没有任何错误的时候，执行else")

finally:
    print("不管有没有错，都执行")