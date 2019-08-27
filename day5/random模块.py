#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import random

print(random.random())               #用于生成一个0到1的随机浮点数：0 <= n < 1.0


print(random.randint(1,7))           #random.randint（）的函数原型为：random.randint（a，b），用于生成一个指定范围内的整数。其中参数“a” 是下限，参数b是上限，生成的随机数n： a <= n <= b


print(random.randrange(1,10))
#random.randrange的函数原型为：random.randrange([start], stop[, step])，
# 从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，
# 结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。
# random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。


print(random.choice('zhangsan'))
#random.choice从序列中获取一个随机元素。
# 其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
# 这里要说明一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。



# 下面是使用choice的一些例子：
print(random.choice('zhangsan'))
print(random.choice(["zhangsan","lisi","wanger"]))  #列表
print(random.choice(("zhangsan","lisi","wanger")))  #元组
print(random.sample([1,2,3,4,5],3))    #列表
#random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。




#随机整数
print(random.randint(0,99))

#随机选取0到100之间的偶数
print(random.randrange(0,101,2))

#随机浮点数
print(random.random())
print(random.uniform(1,10))


#随机字符
print(random.choice('addfsdfsd$#@?'))

#多个字符中选取特定数量的字符
print(random.sample('sfdsfsdfdd',3))

#随机选取字符串
print(random.choice(['apple','pear','peach']))


#洗牌
items = [1,2,3,4,5,6,7,8,9,0]
print(items)
random.shuffle(items)
print(items)