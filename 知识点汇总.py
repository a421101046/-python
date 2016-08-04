1.print函数（打印的函数）
	print 直接加字符串					   						  如 print "hello world"
	print 表达式或变量,表达式或变量 	        					  加 逗号，可以打印多个表达式或变量但不换行	    
	print "存在 一个 %d %s...等格式符,后面要跟上一个同类型的变量"	  如  print "12%d45" % 3
	print "存在多个格式符，后面跟上多个变量"						  如  print "%s%d%d5" %("12",3,4)
	print """  这方式可以打印需要换行的长文本 """    										  

2.字符串格式化
	%r
	%s
	

3.运算符
	+   加号可以对list,str,tuple,dict,float,int,bool等类型进行操作 
		[float/int/bool] + [float/int/bool] ,计算结果向精度高的类型转化(但不会转成bool)    如 True + 1.1  结果为2.1
		[list/str/tuple] + [[list/str/tuple]] "加号两边必须同类型",计算结果返回 同类型的的新集合  如 [1,2,3] + [3,4]  结果为[1,2,3,4,5]
		对 dict不可操作
	
	-   [float/int/bool] - [float/int/bool] 计算结果向精度高的类型转化(但不会转成bool)  		   
		
	*	[float/int/bool] * [float/int/bool]  计算结果向精度高的类型转化(但不会转成bool)
		
		[int/bool] * [tuple/str/list]  进行操作,结果返回同类型的的新集合   如2 * [1,2] 结果为 [1,2,1,2]
		
	/   [float/int/bool] / [float/int/bool]  计算结果向精度高的类型转化(但不会转成bool)
	
	%   [float/int/bool] % [float/int/bool]  计算结果向精度高的类型转化(但不会转成bool)
	
		"[A/B/C] 代表 A,B,C中任选一个"
	
	**  [float/int/bool] **  [float/int/bool]  计算结果向精度高的类型转化(但不会转成bool)
		# ** 相当于 ^

4. 转义字符
	\n 换行符  \t 制表符  \" 相当于一个双引号
	 


5. 获取用户输入
   r = raw_input(a)   r代表输入的内容,a代表输入时的提示(可以不写)
   把每个输入数据,都当成字符串返回 (可以接受任何类型的输入,包括表达式),并且会把字符串多余的' ",进行转义
   
   
6. 命令行命令
	pydoc 查文档   查完 按q退出  , 如pydoc file
	
7.给脚本传参脚本,解包
  如

	from sys import argv   # 将sys模组/库中引入  ,argv是一个参数的变量 , 包含你传递给python的参数

	script, first, second, third = argv   # argv进行解包

	print "The script is called:" , script  # script是脚本名 ,其余是传入的参数
	
	# 在命令行中要执行 python ex13.py  [参数] [参数] [参数] 分别存在first,second,third中
	

8.文件操作
	open(文件名,操作类型,缓存的大小)  """后两个参数可以省略"""
		操作类型有  r(读取  默认caozuo)   w(写入)  a(追加)  b(二进制形式)    U(用于输入通用的换行符)
		
		r操作时,文件必须存在
		b操作时,用于二进制的数据
		w/a操作时,文件不存在会自动创建
		a操作时,往文件中追加文本
		w操作时,将文件清空,再写如文本
		+操作时,文件可读可写,+不能单独使用
		
		
	write(字符串)				
		写入字符串
	read(size)   #不写size参数,代表全部读入
		读取字符串
	close()  
		关闭资源文件
		
	seek(位置)
		设置文件操作的指针位置
	truncate()
		抹除文件内容
		
	# 使用例子如下
	handle = open(filename,"r+") 
	handle.read(3)  			# 一个英文字符 1个字节  一个中文字符 3个字节(可能固定)
	handle.write("aaa")
	handle.close()				# 关闭操作文件的对象

9.定义函数
	def 函数名(参数):  	# 参数可以为空,  :一定要加,  将以下缩进的内容作为函数内容
		print "fsdfds"   
		return 返回值	    # return 代表函数的返回值,当没有return是返回类型为NoneType,返回值为None
	
	def 函数名 (*args):   # 把所有传入的参数放入args,args是一个元组
		arg1,arg2 = args  # 可以先解包,再用	
		args[0]			  # 也可以直接用	
		
	def 函数名 (**args):	 # 把所有传入的参数放入args,args是一个字典,当传入参数不符合要求时,会报错
		print agrs      #  当函数为test时,参数要这样  test(c="test",b="fsdfds")


10. list操作函数
	参见计算机科学和python导论 笔记   第六讲
	
11. 运算符
	
	and 相当于 &&

	or 相当于 || 	

	not 相当于 !	 # 只能对逻辑表达式使用   

	!= 代表不等 
	
	== 代表根据值来判断  
	
	is 根据对象地址即id判断
	
12. list的操作
	arr[1: ] 代表列出第1个元素以后的所有元素  (包含第1个)
	arr[ :-1]  代表列出最后一个元素之前 的所有元素  (不含最后一个) 
	arr[::2]  初始点为0,布长为2,取出对应的元素
	arr[::3]	初始点为0,布长为3,取出对应的元素
	
	arr[::-1]		初始点为最后一个,布长为-1,取出对应的元素,颠倒输出
	arr[::-2]		初始点为最后一个,布长为-2,取出对应的元素,颠倒shuchu
	
	""" 以上输出都是arr的副本  """
	
	append(元素)      可以添加一个元素
	extend(一个list)  把list中的元素全加入
	
	'''写法类似 matlab'''


13. str操作
	同list
	
	.join(list) # 代表将list中元素以#拼接成字符串

14. dict操作
    字典的value可以为任意类型如function dict list  key可以为不可变类型 如tuple int str
	
	"""  print 字典 ,结果是与初始化不一样。因为hashtable """

15. if else语句
	if 表达式:
		语句
	elif 表达式:
		语句
	else 表达式:
		语句
	# else elif可以省略,
	'""详情请见   if else语句的设计注意.py"""

16. 类的定义

class Dinner(object):		# 定义类名 将object当做父类
	def __init__(self):		# __init__ 初始化函数,self指向当前的对象
		"""	设置并初始化成员变量	"""
		self.price = {"宫保鸡丁": 400}
		self.isOK = False
	def	order(self,things): # 定义成员函数 ,self指向当前的对象,things指传入的参数
		print things

	# 例子如下	
	d = Dinner()
	d.order("1")


16. 关键字
	# 详情请见 
	""" 关键字.py"""

9.如何加注释
	# 字符开始是单行注释
	"""  """   '''   '''  一对 三双引号 或三单引号 是代码注释，一般给函数和类加，用于函数参数作用的的介绍
10.设置字符的编码

# -- coding: utf-8 --


12.常用函数
	type  # 获取对象的类型
	len  # 获取list  dict tuple str 的长度
	dir # 打印对象/函数的属性/方法
	
	range
			'''
			range(1,5) 代表从1到5(不包含5)			[1, 2, 3, 4]

			range(1,5,2) 代表从1到5，间隔2(不包含5)	[1, 3]

			range(5) 代表从0到5(不包含5)
			'''
		
	