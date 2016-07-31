# -- coding: utf-8 --
# 函数和变量


def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses !" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers


print "我们能直接传入函数的参数的值"
cheese_and_crackers(20,30)

print "或者传入变量"

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 注意: 函数里的变量和脚本里的变量之间是没有关系