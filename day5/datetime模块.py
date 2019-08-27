#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


import  datetime

print(datetime.datetime.now())              #返回  2019-08-26 17:54:05.237955
print(datetime.datetime.now() + datetime.timedelta(3))   #当前时间 加 “+3” 天  “2019-08-29 17:58:17.313835”
print(datetime.datetime.now() + datetime.timedelta(-3))   #当前时间 减 “-3” 天  2019-08-23 17:59:10.825159
print(datetime.datetime.now() + datetime.timedelta(hours=3))   #当前时间  加 “+3”小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))   #当前时间 加“+30”分钟



c_time = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))      #时间替换

