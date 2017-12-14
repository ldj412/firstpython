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
import time
'a test module'
from tkinter import * #导入Tkinter包的所有内容
import tkinter.messagebox as messagebox


def consumer():
	r = ''
	while True:
		n1 = yield r
		if not n1:
			return
		print('[CONSUMER] Consuming %s...' % n1)
		r = '200 OK'

def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r1 = c.send(n)
		print('[PRODUCER] Consumer return: %s' % r1)
	c.close()

c = consumer()
produce(c)


'''

[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 OK

'''




