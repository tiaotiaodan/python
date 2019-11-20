#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import threading

def hello():
    print("hello, world")

t = threading.Timer(30.0, hello)
t.start( )
