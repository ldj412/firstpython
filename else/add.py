#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

import math

from functools import reduce

import functools

import sys


'a test module'


from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods = ['GET'])
def signin_form():
	return render_template('form2.html')

@app.route('/signin', methods = ['POST'])
def signin():
	username = request.form['usernamekk']
	password = request.form['passwordkk']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html', usernameabc=username)
	return render_template('form2.html', message='bad username or password', username=username)
	
if __name__ == '__main__':
	app.run()
	
#name render_template is not defined




