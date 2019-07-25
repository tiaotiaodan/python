#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

dict = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

while True:
    for i in dict:
        print(i)

    choice = input("请你选择1>>:")
    if choice in dict:
        while True:
            for i2 in dict[choice]:
                print("\t", i2)
            choice2 = input("请你选择2>>:")
            if choice2 in dict[choice]:
                while True:
                    for i3 in dict[choice][choice2]:
                        print("\t", i3)
                    choice3 = input("请你选择3>>:")
                    if choice3 in dict[choice][choice2]:
                        for i4 in dict[choice][choice2][choice3]:
                            print(i4)
                        choice4 = input("最后一层，按q返回>>:")
                        if choice4 == "q":
                            pass
                    if choice3 == "q":
                        break
            if choice2 == "q":
                break
