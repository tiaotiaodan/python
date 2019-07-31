#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
#案例一
def logerr():
    with open("a.txt","a+") as f:
        f.write("end action\n")

def test1():
    print("test1 starting action...")
    logerr()
def test2():
    print("test2 starting action...")
    logerr()
def test3():
    print("test3 starting action...")
    logerr()

test1()
test2()
test3()


#案例二
import  time
def logerr():
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("a.txt","a+") as f:
         f.write("%s end action\n" %time_current)

def test1():
    print("test1 starting action...")
    logerr()
def test2():
    print("test2 starting action...")
    logerr()
def test3():
    print("test3 starting action...")
    logerr()

test1()
test2()
test3()








