#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import multiprocessing
import time

def  f(name):
    time.sleep(2)
    print('hello', name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    p.join()