#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

import math

from functools import reduce

import functools

import sys


'a test module'


from flask import Flask
from flask import request
print('这是第1步')
app = Flask(__name__)
print('这是第2步')
@app.route('/', methods = ['GET', 'POST'])
def home2():
	print('这是第3步')
	return '<h1>主页</h1>'

@app.route('/signin', methods = ['GET'])
def signin_form():
	print('这是第4步')
	return '''<form action = "/signin" method = "post">
		<p><input name="username"></p>
		<p><input name="password" type="password"></p>
		<p><button type="submit">Sign In</button></p>
		</form>'''
		
@app.route('/signin', methods = ['POST'])
def signin():
	print('这是第5步')
	#需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		print('这是第6步')
		return '<h3>Hello, admin!</h3>'
	print('这是第7步')
	return '<h3>Bad username or password.</h3>'
	
print('这是第8步')
if __name__ == '__main__':
	app.run()

# unindent does not match any outer indentation level
	
'''
xxxx
'''

