# -- coding:utf-8 --
# 习题39.对列表的操作

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "这个列表里没有10件物品,给这个列表添加物品"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Year", "Month", "School", "Gross", "Desk"]

while len(stuff) != 10: 	# 判断列表长度 == 10
	next_one = more_stuff.pop()
	print "添加:", next_one
	stuff.append(next_one) 
	print "这里有 %d 件东西"  % len(stuff)

print "对数组进行一些操作"

print stuff.pop()			# 删除list最后一个元素,并返回该元素

print ','.join(stuff)		# 以 ','为间隔符 将数组拼接成字符串

print '#'.join(stuff[3:5])	# 以 '#'为间隔符 取出第3个到第5个元素(不含第5个),拼接成字符串

print dir(list)

"""
	知识点:
	1. ','.join(things) 实际执行的是 join(',',things)
	2.class 是定义类的关键字
	3. dir(things) 用来查看things的方法和属性
	4. OOP 和 函数编程

"""