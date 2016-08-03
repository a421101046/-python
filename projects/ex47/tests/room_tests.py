# -- coding:utf-8 --


from nose.tools import *
from ex47.game import Room   # 被测试的文件必须放在主目录下，即ex47下。只要import 文件名就行


# 这些测试用例是来测试room这个类  用断言判断assert_equal是否成立
def test_room():   
	gold = Room("GoldRoom","""This room has gold in it you can grab.door to the north.""") 
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.") 
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south}) 
	assert_equal(center.go('north'), north) 
	assert_equal(center.go('south'), south)
	
def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")
	
	start.add_paths({'west': west, 'down': down}) 
	west.add_paths({'east': start}) 
	down.add_paths({'up': start})

	assert_equal(start.go('west'), west) 
	assert_equal(start.go('west').go('east'), start) 
	assert_equal(start.go('down').go('up'), start)
	
"""	
当nosetests命令被执行的时候，会自动找到  当前项目/tests的目录，
检测文件名格式为XXX_tests.py中的以test开头的函数和类

创建辅助函数来避免重复的代码。

别太把测试当做一回事。有时候,更好的方法是把代码和测试全部删掉,然后重新设计代码。

"""
