#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import time
import threading

def run(n):
    global  num           #设置每个线程中的获取这个的全局变量
    #print("--get num" ,num)
    time.sleep(1)
    lock.acquire()          #修改数据前加锁
    num -= 1
    lock.release()          #修改数据库释放

num = 50                   #设定一个共享变量
t_objs = [ ]
lock = threading.Lock()      #生成全局锁
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.start()
    t_objs.append(t)


for t in t_objs:         #等待所有线程执行完毕
    t.join()

print("---------------all threads has finished......",threading.current_thread(),threading.active_count())

print("num:",num)