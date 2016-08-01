# -- coding: utf-8 --

# 关于class的构建

class Dinner(object):
	def __init__(self):
		"""		初始化函数,初始化价格	"""
		self.price = {"宫保鸡丁": 400}
		self.isOK = False
		
	def	order(self,things):
		"""		下订单时发生的事情		"""
		if things == "蛋炒饭":
			print "这太low,本店没有"
		elif things == "鲸鱼肉":
			print "呵呵,你在逗我么"
		elif things == "披萨":
			print "这是中式餐厅！！"
		elif things == "宫保鸡丁":
			self.isOK = True
			print "好的,请稍后"
		else:
			print "╰(`□′)╯ ！！"
			
	
	def pay(self,things):
		"""		付款					"""
		print self.price[things]


	def startOrder(self):
		"""		开始下订单			"""
		print("先生请问你点什么!")
		while(not self.isOK):
			things = raw_input('>')
			self.order(things)
		self.pay(things)
		
		
d = Dinner()
# d.startOrder()



# 知识点
"""
	1.self代表类的实例
	2.getattr(对象,属性名,当没有获取到属性名时的默认值)
	如getattr(d,'price')

"""

