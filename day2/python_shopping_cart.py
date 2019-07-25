#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('watch',2000),
    ('booke',20),
    ('Coffee',31),
]

shopping_list = [ ]
salary = input("请你输入数字：")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("选择要买什么东西？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0 :
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart ,your current balance is %s" %(p_item,salary) )
                else:
                    print("你余额不足只剩[%s]，请充值" %(salary))
            else:
                print("你输入该商品不存在!")
        elif user_choice == 'q':
            print("---------shopping list--------")
            for p in shopping_list:
                print(p)
            print("你当前余额:",salary)
            exit()
else:
    print("输入错误，请输入数字！")