# -*- coding: utf-8 -*-


height = 1.75
weight = 80.5

h_1 = input('请输入小明的升高，注意单元为米')
w_1 = input('请输入小明的体重，注意单位是公斤')

w_xm = int(w_1)
h_xm = int(h_1)

BMI = weight / height /height
BMI_xm =w_xm / h_xm /h_xm
if BMI <= 18.5:
	print('过轻')
elif BMI <= 25:
	print('正常')
elif BMI <= 28:
	print('过重')
elif BMI <= 32:
	print('肥胖')
else:
	print('严重肥胖')