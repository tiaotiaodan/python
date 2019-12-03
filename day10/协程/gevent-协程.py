#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import gevent


def func1():
    print('\033[31;1m张三在吃早饭...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m张三在吃晚餐...\033[0m')


def func2():
    print('\033[32;1m李四在吃早饭...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李四在吃晚餐...\033[0m')

def func3():
    print('\033[32;1m王二在网吧...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m王二出网吧了...\033[0m')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    #gevent.spawn(func3),
])