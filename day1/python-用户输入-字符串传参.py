#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")

# info = '''
#
# ------------- info of  %s ------------
# Name: %s
# Age:%s
# Job:%s
# salary: %s
#
# '''   %(name,name,age,job,salary)


info2 = '''

------------- info of  {name} ------------
Name: {name}
Age:{age}
Job:{job}
salary: {salary}

''' .format(name=name,
            age=age,
            job=job,
            salary=salary)
print(info2)