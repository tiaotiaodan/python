#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class A:
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)


b = B()
b.add(2)  # 3




# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break




class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
print(hasattr(point1, 'x'))
print(hasattr(point1, 'y'))
print(hasattr(point1, 'z'))
print(hasattr(point1, 'no'))  # 没有该属性


a = frozenset([1,2,3,4,5,6,7,8,9])
print(globals())
print(a)



def sayhi():
    pass

print(callable(sayhi))


def test():
    print("the is test")

print(callable(test))




a = bytes("abcde", encoding="utf-8")
b =  bytearray("abcde",encoding="utf-8")

print(a)

print(b[1])
b[1] = 50
print(b)



print( ascii([1,2,"你好"]))


# python all函数
print( any([1,-5,3,]))
print( any([ ]))


# python abs函数
print("abs(-45) :", abs(-45))
print("abs(100.12) :", abs(100.12))
print("abs(8) :", abs(8))

#python all函数
print(all([1,-5,3,]))