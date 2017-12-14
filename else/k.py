#!/usr/bin/env python3
# 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
# 在计算机内存中，统一使用Unicode编码，
# 当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# gbkTypeStr = unicodeTypeStr.encode("GBK", 'ignore')
# 在对unicode字符编码时，添加ignore参数，忽略无法编译的字符。
import math
from functools import reduce
import functools
import sys
'a test module'

print('这是第1步')

# 作业
class Student(object):
	def __init__(self, name, score, gender):
		self.name = name
		self.score = score
		self.__gender = gender

	def get_gender(self):
		return self.__gender
		
	def set_gender(self, gender):
		if(gender == 'Male' or gender == 'Female'):
			self.__gender = gender
		else:
			print('please input Male/Female')
	def print_info(self):
		print('%s-%s-%s' % (self.name, self.score, self__gender))
		
a0 = Student('Young', 76, 'Female')
if (a0.get_gender() != 'Female'):
	print('测试失败')
else:
	a0.set_gender('Male')
	if(a0.get_gender() != 'Male'):
		print('Failed!')
	else:
		print('successed')








