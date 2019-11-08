#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

#示例通过valueerror的，修改为indexerror无法处理异常，直接报错
s1 = 'hello'
try:
    int(s1)
except IndexError as  e:
    print(e)


#考虑到上述的无法处理非指定的异常，则无法处理，下面演示可以提前添加考虑的错误try
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)


#万能异常处理案例1
s1 = 'hello'
try:
    int(s1)
except Exception as e:
    print(e)

#第二种处理
s1 = 'hello'
try:
    int(s1)
except KeyError as e:
    print("键错误",e)

except IndexError as e:
    print("索引错误",e)

except Exception as e:
    print("错误")


