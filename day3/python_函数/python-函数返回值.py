#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

def test01():
    pass
def test02():
    return 0
def test03():
    return 0,10,"hello",['alex','lb'],{'wuda','ld'}

t1=test01()
t2=test02()
t3=test03()

print('from test01 return is [%s]:' %type(t1),t1)
print('from test01 return is [%s]:' %type(t2),t2)