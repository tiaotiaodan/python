#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")
print(File_open.tell())

print(File_open.readline())

print(File_open.tell())

File_open.close()               #打印完成后关闭文件