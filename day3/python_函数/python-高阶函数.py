#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


def add(x,y,f):
    return f(x) + f(y)

res = add(3, -6,abs)

print(res)