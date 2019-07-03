#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

name = input("name:")
age = input("age:")
job = input("job:")
salary = input("salary:")


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



info3 = '''

------------- info of  {0} ------------
Name: {0}
Age:{1}
Job:{2}
salary: {3}

''' .format(name,age,job,salary)

print(info3)