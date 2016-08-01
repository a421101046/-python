# -- coding: utf-8 --
# 可爱的字典,字典


# 以下例子表明,list通过数字找到列表元素
things = ['a', 'b', 'c', 'd']
print things				# 结果['a', 'b', 'c', 'd']

things[1] = 'd'		
print things				# 结果['a', 'd', 'c', 'd']


# 以下例子表明, 字典的value可以为list,number,str类型(实际上可以为任意类型). key可以为str类型
# del 实现字典的key - value的删除
stuff = {'name': 'chen', 'age': 22 ,'height': '174'}
print stuff['age']			# 结果 22

stuff['info'] = stuff
print stuff['info']['name'] # 结果 chen 

del stuff['info']			
print stuff['age']			# 结果 22


# 一个有趣的例子
cities = {'温州' : '浙江', '海淀' : '北京', '浦东' : '上海'}
cities['济南'] = '山东'

def find_city(themap, state):
	"""		通过城市名找到省		"""

	if state in themap:
		return themap[state]
	else:
		return "没找到"

cities['_find'] = find_city		# 以'_find'为key,function为value,添加到字典中

while True:
	state = raw_input("请输入城市的名字? 若不想输入请按 enter")
	if not state:
		break
	city_found = cities['_find'](cities, state)
	print city_found



for i in cities:
	print(i)




"""
	dict的无法做到的事情
		字典输出是无序的,因为hashtable


"""


