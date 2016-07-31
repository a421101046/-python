# -- coding: utf-8 --

from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "把%s的文件内容拷贝到%s文件中"  % (from_file, to_file)

# 我们可以完成下面这个两句用一行么

input = open(from_file)

indata = input.read()

print "输入文件的有%d字节数 " % len(indata)

print "输出文件存在么 %r" % exists(to_file)

print "确定拷贝么? 按Enter确定,按CTRL-C中止"

raw_input("?")

output = open(to_file,'w')

output.write(indata)

output.close()

input.close()


# cat  只能在 Linux 和 OSX 下面使用