#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  time
def bar():
    print("in the bar ")

def foo(func):
    start_time=time.time()
    func()
    stop_time=time.time()
    print("the func run time is %s" %(stop_time-start_time))


foo(bar)