#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

user = "zhangsan"
passwd = "zhangsan123"

def test(func):
    def wapper(*args,**kwargs):
        username = input("username:").strip()
        password = input("password:").strip()
        if user  == username and passwd == password:
            print("\033[32;1m user has passed authentication \033[0m")
            res = func(*args,**kwargs)
            print("---after authenticaion")
        else:
            exit("\033[31;1m invalid username or password\033[0m")
    return wapper

@test
def test1():
    print("welcome to index page")

@test
def test2():
    print("welcome to index page")
    return "from home"


test1()
test2()