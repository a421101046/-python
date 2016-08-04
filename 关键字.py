其他Keywords 
 
del	   # 删除list中的一些元素	
  

 
global	# 定义全局变量,若在某个函数内定义,那么函数外也能访问到
		global  b
  
with  as  # with可以用来简化try-finally语句
			with 函数  as 接受__enter__()返回值的对象:
				执行语句
			先执行函数,再调用对象的__enter__(),执行语句,最后调用对象的__exit__()

assert	# 断言 判断一个表示式是否为True，不符合停止运行报错
 
 
pass	# 什么都不要做  
		如class C: pass    # a class with no methods (yet)
		如果不写pass,编译器会报错

yield	# 返回一个生成器

exec	# exec语句用来执行在字符串或文件中的Python语句
		exec 'print "Hello World"'
		
in		# a in arr 在 arr中a存在么

raise	# 抛出异常  raise MyException("error")

lambda  # 匿名函数是个很时髦的概念，提升了代码的简洁程度
		 g = lambda x: x*2 
		 g(3)		




