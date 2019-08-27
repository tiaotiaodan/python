#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import time

print(time.process_time())    #测量处理器运算时间
print(time.altzone)          #返回与utc时间的时间差，以秒计算
print(time.asctime())       #返回时间格式“Mon Aug 26 17:23:29 2019”
print(time.localtime())     #返回本地时间的struct time对象格式
print(time.gmtime(time.time()-80000))    #返回utc时间的struc时间对象格式
print(time.asctime(time.localtime()))     #返回时间格式“Mon Aug 26 17:30:20 2019”
print(time.ctime())                      #返回“Mon Aug 26 17:32:03 2019”的格式，和上面相同


# 日期字符串  转成  时间戳
string_2_struvt = time.strptime("2016/05/22","%Y/%m/%d")      #将  日期字符串   转成  struct时间对象格式
print(string_2_struvt)




#  将时间戳转为字符串格式
print(time.gmtime(time.time() -86640))             #将utc时间戳转换成struct_time格式
print(time.strftime("%Y-%m-%d  %H:%M:%S",time.gmtime()))     #将utc struct_time格式转成指定的字符串格式 “2019-08-26  09:39:30”