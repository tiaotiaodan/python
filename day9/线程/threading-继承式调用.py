#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,n):
        threading.Thread.__init__(self)
        self.n = n

    def run(self):
        print("running on number:%s" %self.n)

        time.sleep(3)

if __name__ ==  '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
