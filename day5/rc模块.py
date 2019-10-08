#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

import  re

res  =  re.match("Chen\d","Chen321Ronghua123")           #从头开始匹配，以Chen\d匹配数字0-9，的一个数字
print(res.group())

res  =  re.match("Chen\d+","Chen321Ronghua123")          #从头开始匹配，以Chen\d+模式匹配，匹配的数字字符可以前一个字符或多个字符
print(res.group())

res  =  re.match("^.*","Chen321Ronghua123")              #从头开始匹配，以什么开头匹配一个字符或多个字符
print(res.group())

res  =  re.match("^.+","Chen321Ronghua123")                #从头开始匹配，以什么开头匹配一个字符或多个字符
print(res.group())

res  =  re.search("3$","Chen321Ronghua123")             #以什么结尾，当前是以3结尾
print(res.group())


res  =  re.findall("[0-9]{1,3}","Chen321Rongh456ua123")             #匹配所有的字符放到以列表中元素返回，匹配所有数字到列表
print(res)

res = re.search("abc|ABC","ABCBabcCDef")                           #“|”管道符是从左到依次匹配，“|”管道符还叫“非”或者“或”意思是只要有一边成立，这个对比就成立
print(res.group())



res = re.sub("[0-9]+","|","abc12de3f45GH",count=2)    #匹配字符并替换
print(res)