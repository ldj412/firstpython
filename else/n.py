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

# 第一个函数是求从a到b的各整数之和
def sum_a(a, b):
	if a>b:
		#print('a+...+b=')
		return 0
	else:
		return a + sum_a(a+1,b)
		
#print('这是第m步')	
#print(sum_a(1,5))

# 第二个函数是求从a到b的立方之和
def cube(x):
	return x*x*x
	
k=2
#print('k=%s' % k)
#print('k^3=%s' % cube(k))

def sum_cube(a, b):
	if a>b:
		##print('a^3+...+b^3=')
		return 0
	else:
		return cube(a) + sum_cube(a+1,b)
		
#print(sum_cube(1,3))

# 第三个函数是求1/((a+2)+(a+4))之和
def pi_sum(a, b):
	if a>b:
		#print('----')
		return 0
	else:
		return (1/a+1/(a+2)) + pi_sum(a+4,b)
		
#print(pi_sum(1,1000))

# maximum recursion depth exceeded in comparion

#定义平方--P8
def square(x):
	return x*x
#print('square(square(3))=%s' % square(square(3)))

def sum_of_squares(x,y):
	return square(x)+square(y)
	
#print('sum_of_squares(3,4)=%s' % sum_of_squares(3,4))

def f1(a):
	return sum_of_squares(a+1, a*2)

#print('f1(5)= %s' % f1(5))

#条件表达式和谓词--P11
def aabs(x):
	if x>0:
		return x
	else :
		return -x
		
#print('aabs(-5)=%s' % aabs(-5))
	
def fangwei(x):
	if (x>5) and (x<10):
		#print('这是第3步')		
		return print('小于10大于5')
	else:
		return print('不在5和10之间')

#print('这是第2步')		
#print(fangwei(4))
#print('这是第4步')	

def fangwei(x):
	if (x>10) or (x<5):
		#print('这是第3步')		
		return print('不在5和10之间')
	else:
		return print('小于10大于5')	
#print('4不在%s' % fangwei(4))

#练习1.5
def p(p):
	return p
	
def test(x,y):
	if x==0:
		return x
	else:
		return y
		
test(0,(p))

# invalid synatax

# 用牛顿逐步逼近法求方根 P15
def good_engough(guess,x):
	return abs(x-square(guess))<0.00001
def average(x,y):
	return (x+y)/2
def improve(guess,x):
	return average(guess, x/guess)
#print(improve(1.5,2))
#print(good_engough(1,1))
def sqrt_iter(guess,x):
	if good_engough(guess,x):
		return guess
	else:
		#print('中间值为：%s' % guess)
		return sqrt_iter(improve(guess,x),x)

def sqrt(x):
	return sqrt_iter(1.0,x)
	
#print('最后的值为：%s' % sqrt(9))
		
# unexpected eof while parsi-ng

# 以下直接把各个方法取消，直接在判断语句和返回
# 语句下进行的修改
def sqrt_a(y,x):
	if abs(x-y*y)<0.001:
		return y
	else:
		return sqrt_a((x/y+y)/2,x)
def sqrt_1(x):
	return sqrt_a(1.0,x)
#print('最后的值为：%s' % sqrt_1(9))

#用牛顿逐步逼近法求立方根 P17
def sqrt_b(y,x):
	if abs(x-y*y*y)<0.001:
		return y
	else:
		return sqrt_b((x/y/y+2*y)/3,x)
def sqrt_2(x):
	return sqrt_b(1.0,x)
#print('最后的值为(立方根)：%s' % sqrt_1(9))


	












