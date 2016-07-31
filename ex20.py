# -- coding: utf-8 --
# 函数和文件
from sys import argv

script,input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0) # 参数代表字节数
	
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "首先打印整个文件"

print_all(current_file)

print "重新回到起始页"

rewind(current_file)

print "接着用rewind打印三行"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

