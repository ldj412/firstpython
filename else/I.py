# -*- coding: utf-8 -*-

import math

from functools import reduce



def fib(max):
	n, a, b =0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	print('done')
	return
f = fib(6)
print(next(f))
print(next(f))
print(next(f))
#print(f)
