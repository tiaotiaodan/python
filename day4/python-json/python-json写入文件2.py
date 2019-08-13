#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  json


info = {
    'name':'zhangsan',
    'age':'26',
}

f = open("test2.txt","w")
f.write( json.dumps(info))

f.close()