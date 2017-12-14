# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	deta_1 = b * b - 4 * a * c
	if deta_1 >=0:
		x = (-b + math.sqrt(deta_1)) / (2 * a)
		y = (-b - math.sqrt(deta_1)) / (2 * a)
		return(x, y)
	else:
		print('无解')
		return('无解','无解')

a1= int(input('请输入a'))
b1= int(input('请输入b'))
c1= int(input('请输入c'))

t = quadratic(a1, b1, c1)

print(quadratic(a1, b1, c1))

# math domain error
# nonetype object is not subscriptable
