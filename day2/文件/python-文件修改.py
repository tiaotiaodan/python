#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

f = open("file","r",encoding="utf-8")
f_new = open("file.txt","w",encoding="utf-8")

for line in f:
    if "昨日当我年少轻狂"  in  line :
        line = line.replace("昨日当我年少轻狂","今日的抓狂的我！")
        f_new.write(line)
    else:
        f_new.write(line)
f.close()
f_new.close()