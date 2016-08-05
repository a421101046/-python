# -- coding:utf-8 --

class binaryTree(object):
    def __init__(self, value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None 
    def setLeftBranch(self, node):
        self.leftBranch = node
    def setRightBranch(self, node):
        self.rightBranch = node
    def setParent(self, parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return str(self.value)


# 广度优先
def BFS(root,val):
	''' root 是根节点,val是希望找的值 '''
	list = [root]      # 将根节点放入栈中
	while(len(list) > 0):
		# 栈中第一个节点符合么
		if list[0].getValue() == val:  # 这里需要判断 0索引是否存在
			return True
		else: # 不符合pop第一个
			fatherNode = list.pop(0)
			
			# 先将左节点入队列
			if fatherNode.getLeftBranch():
				list.append(fatherNode.getLeftBranch())
			
			# 先将右节点入队列
			if fatherNode.getRightBranch():
				list.append(fatherNode.getRightBranch())

		# 当list为空,停止循环
	return False

def getPath(root):
	'''
		获取节点的路径
	'''
	if not root.getParent(): # 当没有父节点,便是根节点
		return [root.getValue()]
	else:
		return [root.getValue()] + getPath(root.getParent())
		
		
def DTreeBuild(added,needAdd):
	'''   added已经添加的物品列表  	list类型  
	needAdd 需要被添加的物品列表   list类型   
	函数返回DecisionTreeBuild  创建决策树    '''
		
	# 当没有物品可以添加的时候 直接返回一个内容为空的节点
	if(len(needAdd) == 0):		
		return binaryTree([])

	curNode = binaryTree(added) # 根据added  needAdd创建 当前的节点
	
	leftBranch = DTreeBuild(added + needAdd[0:1],needAdd[1:]) # 往背包添加下一件物品
	rightBranch = DTreeBuild(added,needAdd[1:])				#  确定背包不需要下一件物品
	curNode.leftBranch = leftBranch
	curNode.rightBranch = rightBranch
	
	return curNode
	
def DFSDTree(root,isBest,isExceed):
	''' isBest 是function类型  判断这个方案是不是最好的方案
	isExceed   是function类型  判断这个方案有没有超过重量/限制
	root		是决策树的根节点
	return 		该函数返回list 存放最好的方案
	
	本函数利用深度遍历寻找最佳的方案,需要遍历所有节点
	
	'''
	stack = [root]
	best = []
	
	while(len(stack) > 0): # 判断栈中有没有东西
		project = stack[0]
		if (isExceed(project.getValue())): # 是否超出重量 下面的分支就不要了
			stack.pop(0)		# pop旧的节点
			continue			
				
		if(isBest(project.getValue(),best)): # project方案更好替换best,
			best = project.getValue()
			
		stack.pop(0)
		if project.rightBranch:			# 将右分支入栈
			stack.insert(0,project.rightBranch)		
		if project.leftBranch: 			# 将左分支入栈
			stack.insert(0,project.leftBranch)						
	return best
		
def BFSDTree(root,isBest,isExceed):
	queue = [root]
	best = []
	
	''' isBest 是function类型  判断这个方案是不是最好的方案
	isExceed   是function类型  判断这个方案有没有超过重量/限制
	root		是决策树的根节点
	return 		该函数返回list 存放最好的方案
	
	本函数利用广度遍历寻找最佳的方案,需要遍历所有节点
	
	'''
	
	while(len(queue) > 0): # 判断栈中有没有东西
		project = queue[0]
		if (isExceed(project.getValue())): # 是否超出重量 下面的分支就不要了
			queue.pop(0)		# pop旧的节点
			continue			
				
		if(isBest(project.getValue(),best)):
			best = project.getValue()	 # project方案更好替换best,
			
		queue.pop(0)
		if project.leftBranch: 			# 将左分支入栈
			queue.append(project.leftBranch)	
		if project.rightBranch:			# 将右分支入栈
			queue.append(project.rightBranch)		
							
	return best


def isBest(pro1,pro2):
	'''  比较两个集合哪个价值更高 '''
	sum1 = 0
	sum2 = 0
	for item1 in pro1:
		sum1 += item1[1]
	for item2 in pro2:
		sum2 += item2[1]
	return sum1 > sum2
	
def isExceed(pro):
	''' 比较方案的重量有没有超过 限制要求  限制10'''
	weight = 0
	for item in pro:
		weight += item[2]
	return weight > 10	# 有没有超过10
	
def isOK(pro):
	''' 比较方案的价值是否 可用'''
	value = 0
	for item in pro:
		value += item[1]
	return value > 8  # 价值有没有超过8

def BFSBetterDTree(root,isBest,isExceed,isOK):
	queue = [root]
	best = []
	
	''' isBest 是function类型  判断这个方案是不是最好的方案
	isExceed   是function类型  判断这个方案有没有超过重量/限制
	root		是决策树的根节点
	isOK	  是function类型  判断这个方案是否可用,按照价值判断
	return 		该函数返回list 存放可用的方案
	
	本函数利用广度遍历寻找可用的方案,不需要遍历所有节点
	
	'''
	
	while(len(queue) > 0): # 判断栈中有没有东西
		project = queue[0]
		if (isExceed(project.getValue())): # 是否超出重量 下面的分支就不要了
			queue.pop(0)		# pop旧的节点
			continue			
				
		if(isBest(project.getValue(),best)):
			best = project.getValue()	 # project方案更好替换best,
		
		if(isOK(project.getValue())):
			break
			
		queue.pop(0)
		if project.leftBranch: 			# 将左分支入栈
			queue.append(project.leftBranch)	
		if project.rightBranch:			# 将右分支入栈
			queue.append(project.rightBranch)		
							
	return best	
	
	
def ImplicitDTree(needadd,space):
	'''
		needadd代表还没添加的物品列表   ("锤子",value,weight)
		space代表剩余的空间
		
		返回 隐性决策树,不生成所有节点的决策树,
	'''
	if len(needadd) == 0 or space <= 0:
		return [0,[]]  # 价值  方案
	
 	# 往背包添加下一件物品
 	need_values,need_projects = ImplicitDTree(needadd[1:],space - needadd[0][2])
	
 	# 确认这件物品背包不要的情况
 	no_values,no_projects = ImplicitDTree(needadd[1:],space)
		
	
	if need_values + needadd[0][1] > no_values:
		need_projects.append(needadd[0])
		return [need_values + needadd[0][1],need_projects]
	else:
		return [no_values,no_projects]
	
	