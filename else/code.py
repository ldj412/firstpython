#!/usr/bin/env python3
# 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*-
# 在计算机内存中，统一使用Unicode编码，
# 当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
# 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# gbkTypeStr = unicodeTypeStr.encode("GBK", 'ignore')
# 在对unicode字符编码时，添加ignore参数，忽略无法编译的字符。


"""
这篇专门用来将py文件转换成编译后的字节码指令
"""

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>hello, %s!!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]