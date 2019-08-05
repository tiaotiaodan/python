#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  time

def test(func):                                      #test=(test1)  func=test1
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print("the func run time is  %s"  %(stop_time-start_time))
    return deco

@test                       #test1=test(test1)
def test1():
    time.sleep(1)
    print("in the test1")

@test                      #test2=test(test1)
def test2(name,age):
    time.sleep(3)
    print("in the test2",name,age)


test1()
test2("zhangsan",23)
