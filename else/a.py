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
import time

print('这是第1步')
def func(n):
	print('这是第5步')
	for i in range(0,n):
		print('这是第6步')
		print('这是第9步:', i)
		arg = yield i
		print('这是第10步age：', arg)
		print('这是第7步')
		
		
print('这是第2步')
f = func(10)
while True:
	print('这是第3步')
	print(next(f))
	print('这是第4步')
	f.send(100)
	#time.sleep(1)
print('这是第8步')

# 1,2,3
#next：5,6,9，4
#send：10,7,6,9，3
#next：10,7,6，9,4
#send：10,7,6,9，3




















