# -- coding:utf-8 --

def add(a, b):
	print "加法%d + %d"  %(a, b)
	return a + b

def subtract(a, b):
	print "减法 %d - %d" %(a, b)
	return a - b
	
def multiply(a, b):
	print "乘法 %d * %d" %(a, b)	
	return a * b

def divide(a, b):
	print "除法 %d / %d"  %(a, b)
	return a / b
	
	
print "让我们做一些加减乘除"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
IQ = divide(100, 2)

print "age:%d, height:%d, weight:%d, IQ:%d"  %(age, height, weight, IQ)

# 老是落 ％号