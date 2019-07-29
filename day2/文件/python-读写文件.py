#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")    #文件句柄  读写
File_open = open("file",mode="w+",encoding="utf-8")    #文件句柄   写读
File_open = open("file",mode="a+",encoding="utf-8")    #文件句柄   追加读写
File_open = open("file",mode="rb",encoding="utf-8")    #文件句柄   二进制文件

print(File_open.readline())
print(File_open.readline())
print(File_open.readline())
print(File_open.tell())
File_open.seek(178)
File_open.write("-------------------我是分隔符------------------------")

print(File_open.readline())