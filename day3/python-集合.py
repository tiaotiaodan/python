#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py


list_1 = [ 1,4,5,7,3,6,7,9]
list_1 = set(list_1)

list_2 = set([2,6,0,66,22,8])

print(list_1,list_2)


#交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

#并集
print(list_1.union(list_2))
print(list_1 | list_2)

#差集
print(list_1.difference(list_2))
print(list_1 - list_2)

#子集
print(list_1.issubset(list_2))

#对称差集，就是把双方没有的取出来
print(list_1.symmetric_difference(list_2))
print(list_1 ^list_2 )

#查询set的长度
print(len(list_1))

#查看测试10是不是list_1的成员
print(10 in list_1)

#查看测试10不是list_1的成员
print(10 not in list_1)
