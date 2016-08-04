# -- coding: utf-8 --

from sys import argv 

script ,filename = argv

txt = open(filename)	# 打开文件,返回操作文件的对象

print "这是你的文件名 %s" % txt

print txt.read(3)  		# 读取三个字节

print "再输入一下文件名"

file_again = raw_input("> ")

txt_again = open(file_again) 

print txt_again.read()


txt.close()				# 关闭操作文件的对象
txt_again.close()


# 写代码不严谨,经常落东西

# 知识点  read(字节数)  英文单词 一个字节  中文3个字节