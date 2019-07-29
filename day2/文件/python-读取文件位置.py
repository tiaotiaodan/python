#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")
print(File_open.tell())

print(File_open.readline())
print(File_open.readline())
print(File_open.readline())

print(File_open.tell())       #tell() 方法返回文件的当前位置，即文件指针当前位置。

File_open.seek(0)     # 重新设置文件读取指针到开头
print(File_open.readline())   #读取文件行数，读取一行