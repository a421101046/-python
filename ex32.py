# -- coding: utf-8 --
# 习题32: 循环和列表


# 创建list => 数组
hairs = ['红色', '白色', '绿色']

heights = [132, 123, 43]

elements = [] # 创建空list  添加元素
elements.append('名字') 

# for in 循环
for hairColor in hairs:   # hairColor 是 list 中元素
	print "这个头发的颜色是 %s" % hairColor 

for height in heights:   # height 是 list 中元素
	print "这个人的身高是 %s" % height
	
for i in range(0, 5):	# range生成  从0到5的数组(不包含5)
	print(i)
	elements.append(i)
	
print(heights[::-2])


# range知识点
	
"""

range(1,5) 代表从1到5(不包含5)			[1, 2, 3, 4]

range(1,5,2) 代表从1到5，间隔2(不包含5)	[1, 3]

range(5) 代表从0到5(不包含5)

heights[1: ] 代表列出第1个元素以后的所有元素  (包含第1个)

heights[ :-1]  代表列出最后一个元素之前 的所有元素  (不含最后一个) 


hairs[::2]  初始点为0,布长为2,取出对应的元素
[红色,白色]

array[::3]	初始点为0,布长为3,取出对应的元素
[红色]


颠倒输出

array[::-1]		初始点为最后一个,布长为-1,取出对应的元素
['绿色','白色','红色']

>>> array[::-2]
['绿色','红色']	初始点为最后一个,布长为-2,取出对应的元素

以上输出的都是数组


写法类似 matlab
"""


