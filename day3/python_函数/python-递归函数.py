#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


def calc(n):
    print(n)
    if int(n/2) ==0 :
        return  n
    return  calc(int(n/2))

calc(20)