#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

def test1(x,y):
    print(x,y)

test1(1,2)   #位置参数必须按照顺序固定位置
test1(y=2,x=1)   #关键参数无序固定位置