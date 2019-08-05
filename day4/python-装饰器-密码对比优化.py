#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import time

user, passwd = 'zhangsan', 'zhangsan123'


def auth(auth_type):
    print("auth func:", auth_type)

    def outer_wrapper(func):
        def wapper(*args, **kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and password == password:
                    print("\033[32;1m user has passed authentication \033[0m")
                    res = func(*args, **kwargs)
                    print("---after authenticaion")
                else:
                    exit("\033[31;1m invalid username or password\033[0m")
            elif auth_type == "ldap":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and password == password:
                    print("\033[32;1m user has passed authentication \033[0m")
                    res = func(*args, **kwargs)
                    print("---after authenticaion")
                else:
                    exit("\033[31;1m invalid username or password\033[0m")

        return wapper

    return outer_wrapper


@auth(auth_type="local")
def index():
    print("welcome to index page")


@auth(auth_type="ldap")
def home():
    print("welome to home page")
    return "from home"


index()
home()
