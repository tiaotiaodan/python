#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import threading
import time
import random

event = threading.Event()

def light():
    count = 0
    event.set()
    while True:
        if count > 5  and count < 10:
            event.clear()
            print('\033[41;1m--red light on---\033[0m')
        elif count > 10:
            event.set()
            count = 0
        else:
            print('\033[42;1m--green light on---\033[0m')
        time.sleep(1)
        count +=1
def car(n):
    while True:
        if event.isSet(): #绿灯
            print("car [%s] is running...." % n)
            time.sleep(1)
        else:
            print("car [%s] is waiting for the red light.." % n)
            event.wait()
            print("car [%s] green light is on ,start going.." % n)

if __name__ == '__main__':
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(1):
        t = threading.Thread(target=car,args=(i,))
        t.start()