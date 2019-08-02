#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

x=0
def gpandpa():
    def dad():
        x=2
        def son():
            x=3
            print(x)
        son()
    dad()
gpandpa()


