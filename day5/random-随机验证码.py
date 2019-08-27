#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import random

checkcode=''

for  i  in range(5):
    current = random.randint(0,5)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode+=str(temp)
print(checkcode)