# -- coding: utf-8 --

# 命名 变量 代码 函数
# 函数可以给代码的片段命名,并可以接受参数,可以通过#1 和 #2 可以让你创建微型的脚本




def print_two(*args):	# def 函数名(*args): 之后 缩进的四行都是函数的内容	
	arg1,arg2 = args	# 解参数包
	print "arg1: %r,arg2: %r " % (arg1,arg2)
	
def print_two_again(arg1,arg2):
	print "arg1: %r,arg2: %r " % (arg1,arg2)
	
# 只带一个参数
def print_one(arg1 )  :
	print "arg1: %r" %arg1
	
# 不带参数
def print_none():
	print "I got nothing" 
  	print "I got nothing"
print "I got nothing" 


print_two   ("Chen","WenHua")

print_two_again("Chen","WenHua")

print_one("WenHua")

print_none()

	
