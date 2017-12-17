#!/usr/bin/env python3
# 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
# 在计算机内存中，统一使用Unicode编码，
# 当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# gbkTypeStr = unicodeTypeStr.encode("GBK", 'ignore')
# 在对unicode字符编码时，添加ignore参数，忽略无法编译的字符。
import math
from multiprocessing import Process
import os

# 子程序要执行的代码
"""
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
	print('parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('child process will start.')
	p.start()
	p.join()
	print('child process end')
"""
def consumer():
	print('这是第1步')
	r = ''
	while True:
		print('这是第2步')
		n = yield r
		print('这是第k步')
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		r = '200 OK'
print('这是第3步')
def produce(c):
	print('这是第4步')
	c.send(None)
	n = 0
	while n < 5:
		print('这是第5步')
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n+1)
		print('这是第6步')
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()
print('这是第7步')
c = consumer()
print('这是第8步')
produce(c)






















