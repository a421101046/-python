# -- coding: utf-8 --
# 习题 45: 对象、类、以及从属关系
# 针对类和对象  "is_a" 讨论两个类的共同点		“has_a”指 两个类无共同点,仅仅供互相参照


# is_a
class Animal(object):
	pass
	

class Dog(Animal):
	def __init_(self, name):
		# has_a
		self.name = name
		
# is_a
class Cat(Animal):
	def __init__(self, name):
		# has_a
		self.name = name

# is_a
class Person(object):
	def __init__(self, name):
		# has_a
		self.name = name
	
		# Person has_a pet的属性
		self.pet = None


# is_a
class Employee(Person):
	def __init__(self, name, salary):
		# ????
		super(Employee, self).__init(name)
		
		# has_a
		self.salary = salary

# is_a
class Fish(object):
	pass # ??
	
	
# is_a	
class GoldFish(Fish):
	pass
		
		
# is_a
dog = Dog("哈士奇")
Tom = Cat("汤姆")
linqi = Person("林奇")

# has_a
linqi.pet = Tom




"""
	1.python添加object类的目的是,要求所有子类都从object这个类中继承
	2.？？
	6.存在多重继承  has_many,尽量避免使用


"""
	
		
		