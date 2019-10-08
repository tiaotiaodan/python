#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:shichao
# File: .py

class SchoolMember(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        -------------  info of Teacher: %s -------------
        name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))


    def teach(self):
        print("%s is teaching course [%s] "  %(self.name,self.course))

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        -------------  info of Student: %s -------------
        name:%s
        Age:%s
        Sex:%s
        stu_id:%s
        grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tution for $%s" % (self.name,amount))






t1 = Teacher("zhangsan",34,"M",2000,"linux")
t2 = Teacher("lisi",26,"M",1800,"python")


s1 = Student("wanger",20,"MF",1001,"python")
s2 = Student("maze",20,"MF",1002,"linux")


t1.tell()
