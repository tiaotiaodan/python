#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")

for a,i in enumerate(File_open.readlines()):
    if a == 10:
        break
    print(i.strip())

count = 0
for i in File_open:
    if count == 9 :
        print("-------------------------------我是分割线------------------------")
        count += 1
        break
    print(i)
    count += 1