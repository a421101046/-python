# -- coding:utf-8 ---
# -- coding:utf-8 --

from temp3 import *

n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)



# print DFS(n5,100)

#  ("锤子",1,3) 第二个参数代表价值 第三个代表重量 
DTree = DTreeBuild([],[("锤子",1,3),("手表",2,1),("黄金",5,3),("身份证",4,1),("ipad",3,3),("不知名的钥匙",3,2)])
best = BFSDTree(DTree,isBest,isExceed)
for item in best:
	print item[0] + "价值:"+ str(item[1]) + "  重量:"+str(item[2])

