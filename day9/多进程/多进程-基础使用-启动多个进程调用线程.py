#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import multiprocessing
import time
import threading

def thr_run():
    print(threading.get_ident())

def  f(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thr_run,)
    t.start()


if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=f, args=('bob  %s' %i,))
        p.start()
        #p.join()