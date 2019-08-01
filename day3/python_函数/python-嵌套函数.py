#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

name = "zhangsan"

def change_name():
    name = "lisi"

    def change_name2():
        name = "wangwu"
        print("第三层函数打印",name)

    change_name2()
    print("第二层函数打印",name)


change_name()
print("打印第一层函数",name)