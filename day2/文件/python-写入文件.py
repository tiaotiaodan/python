#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")

File_open.write("我要创建文件")
File_open.write("python read file is name")

data = File_open.read(1)               #从文件开始读取，读取到最后一行，如果不给指定或为负则读取读取所有
print(data)                     #打印读取所有的数据

File_open.close()               #打印完成后关闭文件