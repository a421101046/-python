# -- coding: utf-8 --

from sys import argv 

script ,filename = argv

txt = open(filename)

print "这是你的文件名 %s" % txt

print txt.read(3)

print "再输入一下文件名"

file_again = raw_input("> ")

txt_again = open(file_again) 

print txt_again.read()


txt.close()
txt_again.close()


# 写代码不严谨,经常落东西

# 知识点  read(字节数)  英文单词 一个字节  中文3个字节