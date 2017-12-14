#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

import math

from functools import reduce

import functools

import sys

'a test module'

print('这是第1步')

from types import MethodType
"""
文件名 class2.py
Methodtype 测试
"""
# 首先看第一种方式
# 创建一个方法
def set_age(self, arg):
	self.age = arg
	print(self.age)
#创建一个类
class Student(object):
	pass

#----------以上为公共部分

s_one = Student()
# 给student创建一个方法，但这个不是在class里创建而是
# 创建了一个链接把外部的set_age方法用链接到student内
s_one.set_what = MethodType(set_age,Student)
"""
用MethodType将方法绑定到类，并不是将这个方法直接写到
类内部，而是在内存中创建一个link指向外部的方法，在创
建实例的时候这个link也会被复制。
"""
s_one.set_what(32)
# >>>>>>结果是 32
"""
s_two = Student()
s_two.set_age(100) #这个用来验证下是在类内的方法还是在类外的方法
# >>>>>结果显示：‘Student’ object has no attribute 'set_age'
"""

"""
来看另外一种
"""
#直接用类来创建一个方法，不过此时还是用链接的方式在类
#外的内存中创建
Student.set_ff = MethodType(set_age,Student)
#此时在创建实例的时候外部方法 set_age 也会复制，这些实例
#和Student类都指向同一个set_age方法
new1 = Student()
new2 = Student()
new3 = Student()
new1.set_ff(99)
new2.set_ff(98) #第二个会覆盖第一个
print(new1.set_ff,new2.set_ff)