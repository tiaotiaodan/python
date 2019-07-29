#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

File_open = open("file",mode="r+",encoding="utf-8")


print(File_open.encoding)    #打印文件编码

print(File_open.fileno())    #返回一个文件编号

print(File_open.flush())     #强制刷新缓存到磁盘

File_open.close()
print(File_open.closed)      #判断文件是否关闭了，返回 False或True


File_open.truncate(10)   #不写就清空文件内容，指定内容就清空阶段以前的内容
