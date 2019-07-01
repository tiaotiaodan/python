#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import sys

#案例-迭代器
test = [1,2,3,4]
test1 = iter(test)
for i in test1:
    print(i,end="")




#案例-生成器

test = [1,2,3,4]
test1 = iter(test)
while True:
    try:
        print(next(test1))
    except StopIteration:
        sys.exit()