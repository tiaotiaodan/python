#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

g = ( x *  x for x in  range(5))
for n in g :
    print(n)





L = [x * x for x in range(5) ]
print(L)


g = (x * x for x in range(5) )
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))




