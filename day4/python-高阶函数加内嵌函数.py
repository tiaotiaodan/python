#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  time

def test(func):
    def deco():
        start_time=time.time()
        func()
        stop_time=time.time()
        print("the func run time is  %s"  %(stop_time-start_time))
    return deco

def test1():
    time.sleep(3)
    print("in the test1")

def test2():
    time.sleep(3)
    print("in the test2")


test3=test(test1)
test3()


