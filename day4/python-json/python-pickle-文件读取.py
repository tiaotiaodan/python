#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import pickle

def sayhi(name):
    print("hello",name)


f = open("test1.txt","rb")

data = pickle.loads(f.read())

print(data)