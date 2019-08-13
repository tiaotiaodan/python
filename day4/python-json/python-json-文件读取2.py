#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py
import  json

f = open("test.txt","r")

data = json.load(f)

print(data["age"])


f.close()

