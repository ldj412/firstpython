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

""" 面向高级对象编程
    使用__slots__
"""
# 定义一个类，空类
"""
class Student(object):
	pass
s = Student()
def set_age(self,age):
	self.age_a = age+1
from types import MethodType
s.set_b= MethodType(set_age,s) #给实例绑定一个方法
s.set_b(25)
print(s.age_a)
"""

""" 面向对象编程
    类和实例
"""
class Student(object): #定义类，从object类继承过来的
	pass
bart=Student()   
#创建类的实例，变量bart指向的是一个Student的实例
#print(bart)
bart.name = 'bart simpson' #给一个实例绑定属性
#print(bart.name) 

#通过特殊的方法（__init__方法）在定义类时就绑定方法
class Student_a(object):
	
	def __init__(self,N,S):
		# init 方法的第一个参数永远是self，表示创建的实例本身。
		self.name = N
		self.score = S
#有了__init__方法，创建实例时，就不能传入空的参数
bart_a = Student_a('bart simpson_aa',50)
#print(bart_a.name)
#print(bart_a.score)

""" 面向对象编程
    数据封装
"""
# 每个实例有自己的属性--实例（方法--类），可以通过函数来访问这些实例的属性
# 方法和函数的区别，属于类的函数就是方法
def print_score(std):  #定义一个方法
	print('%s: %s' % (std.name, std.score))
#print_score(bart_a)
# 可以在类内部定义函数，这些函数与类相关联，就成为类的方法。
class Student_a(object):
	def __init__(self_a, S, A):
		self_a.name = S
		self_a.score = A
	def print_a(aaa): #在类里的方法，第一个参数都表示创建的实例本身
		aaa.score = aaa.score+2
		print('%s: %s' % (aaa.name, aaa.score))
	def get_grade(bbb):
		if bbb.score >= 90:
			return 'A'
		elif bbb.score >=60:
			return 'B'
		else:
			return 'C'	
s_a = Student_a('n_a', 98)
#s_a.print_a()

# 可以给类增加新的方法
lisa = Student_a('lisa', 62)
bbcd = Student_a('bbcd', 30)
#print(lisa.get_grade())
#print(bbcd.get_grade())

#小结
# 类是创建实例的模板，而实例是一个一个具体的对象
# 各自实例拥有的数据都相互独立，互不影响。
# 方法就是与实例绑定的函数，与普通函数不同，方法可以直接访问实例的数据


""" 面向对象编程
    访问限制
"""
bart_b = Student_a('bart----a',88)
#print(bart_b.score)
# 在class内部，可以有属性和方法，而外部代码可以直接调用
# 实例变量和方法来操作数据
# 外部代码可自由修改一个实例的name、score属性
bart_b.score=25
#print(bart_b.score)
#print('这是开始')
class Student_b(object):
	#print(' 进入类里面')
	def __init__(m, k, p):
		#print('  定义强制内部属性')
		m.__name = k
		m.__score = p
	#def print_score_a(m):
		#print('  定义打印程序')
		#print('%s: %s' % (m.__name, m.__score))
	def get_name(m2):
		#print('  内部属性传递给共用属性a')
		return m2.__name
	def get_score(m2):
		#print('  内部属性传递给共用属性b')
		return m2._score
	def set_score_a(m3,score):
		#print('  外部属性判断是否符合要求')
		if 0<= score <= 100:
			m3.__score=score
		else:
			raise ValueError('bad score')
	#print(' 准备从类的里面出去')
#print('类的外面')
bart = Student_b('work', 84)
#print('实例赋值完')
#print(bart.set_score_a(90))
# 实例变量后面的点后面带括号则识别为方法，不带括号则识别为属性
bart_d = Student_b('maomao',-5)
bart_d.set_score_a(89)
# unorderable tupes:int()


class Animal(object):
	def run(self):
		print('Animal is running')
class Dog(Animal):
	def run(self):
		print('Dog is running')
	pass
class Cat(Animal):
	def eat(self):
		print('eating meat')
	pass
dog = Dog()
#dog.run()
cat = Cat()
#cat.run()
#cat.eat()
#print(isinstance(dog, Dog))
#print(isinstance(cat, Animal))

def run_twice(k):
	k.run()
	k.run()
#run_twice(Animal())
#run_twice(Dog())

class Tortoise(Animal):
	def run(self):
		print('Tortoise is runnint slowly')

#run_twice(Tortoise())


""" 面向对象编程
    实例属性和类属性
"""
# 实例属性和类属性
# 实例属性就是定义在类的方法里的定义
# 类属性就是在实例里定义的
class Student_c(object):
	name = 'Student0'
	def __init__(self, name):
		self.name = name
#s_c = Student_c('bob')
#print(s_c.name)
#print(Student_c.name)
#s_b = Student_c('off')
#print(s_b.name)
#s_b.name = 'on'
#print(s_b.name)
#del s_b.name
#print(s_b.name)
#del s_b.name
#print(s_b.name)

#练习
#为了统计学生人数，可以给Student类增加一个属性，
#每创建一个实例，该属性自动增加
class Student_d(object):
	cnt = 0
	def __init__(self,name):
		self.name = name
		Student_d.cnt = Student_d.cnt + 1
		
s_d = Student_d('wang')
print(Student_d.cnt)
s_e = Student_d('li')
print(Student_d.cnt)

""" 面向对象高级编程
    使用__slots__
"""

class Student0(object):
	pass
	
s_f = Student0



