# -- coding: utf-8 --

# 需要记住的命令 close read readline truncate  write(stuff)


from sys import argv 

script, filename = argv


print "我将会抹去 %s文件的内容 " %filename

print "如果你不想这样,请按Ctrl + C"
print "如果你想这样,请按 Enter"

raw_input("?")

print "打开文件"

target = open(filename,'w')

print "清空文件"

target.truncate()
# 此时文件内容并未清除

print "现在我需要你输入三行内容"

line1 = raw_input("line 1:")

line2 = raw_input("line 2:")

line3 = raw_input("line 3:")

print "我将开始写入"

target.write("line1:" + line1 + "\n" + "line2:" + line2 + "\n" + "line3:" + line3 )


target.close()


# 知识点 open(filename,'w') 指定写入文件