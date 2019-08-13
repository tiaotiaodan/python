#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  pickle

def sayhi(name):
    print("hello",name)


info = {
    'name':'zhangsan',
    'age':'26',
    'func' :sayhi
}

f = open("test1.txt","wb")
f.write(pickle.dumps(info))
f.close()

