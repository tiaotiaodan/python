#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

names = [ "shichao", "aa"," bb","cc","cc","dd","ee","ff" ]


#切片
print(names[0])
print(names[1:2])
print(names[0:2])
print(names[1:-1])
print(names[1:])
print(names[-1:])

#插入
names.insert(1,"强行从aa前面插入")
print(names)

#追加
names.append("我是新来的")
print(names)

#修改
names[2] = "该换人了"
print(names)

#删除
del  names[3]
print(names)

names.remove("shichao")   #删除指定元素
print(names)

names.pop()    #删除列表最后一个值
print(names)

#扩展
b=[1,2,3,3,45,4,6,7,4,8,]
names.extend(b)
print(names)

#拷贝
names_copy = names.copy()
print(names_copy)


#统计
print(names_copy.count("cc"))


#获取下标
print(names.index("dd"))



# #排序和翻转
# names.sort()
# print(names)

