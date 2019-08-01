#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

# *args: 接受N个位置参数，转换成元组的方式
def test(name,age,*args):    # *args 会把多传入的参数变成一个元组形式
    print(name,age,args)


test("aa",22)

#输出
# aa 22 ()   #后面这个()就是args,只是因为没传值,所以为空

test("aa",22,"acb")

#输出
#  aa 22 ('acb',)


# **kwargs：把N个关键字参数，转换成字典的方式

def test(name,age,*args,**kwargs):    # **kwargs 会把多传入的参数变成一个dict形式
    print(name,age,args,kwargs)

test("zhansan",21,"china","chengdu")

#输出
#  zhansan 21 ('china', 'chengdu') {}    #提示后面这个{}就是kwargs为空，因为我们没传递关键字参数，所以为空

test("zhansan",21,"china",sex="chengdu")

#输出结果

#zhansan 21 ('china',) {'sex': 'chengdu'}   #提示后面这个{'sex': 'chengdu'} ，传递了关键子参数，转化为字典




