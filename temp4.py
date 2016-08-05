# -- coding: utf-8 --

a = [2,3,4,5,6,10,20,50,500,604,1000]
val = 1000

def binarySearch(arr,val):
	left = 0 
	right = len(arr) - 1
	while(left < right):
		mid = (left + right) / 2
		if arr[mid] == val:
			return True
		elif arr[mid] > val:
			right = mid		# 固定写法  因为  (0 + 1) / 2 =0
		else:
			left = mid + 1  # 固定写法  因为  (0 + 1) / 2 =0

	return left == right and arr[left] == val  
	''' 代码执行到这有两个情况 
		进入了while   left 必等于right
		没进入while   left >= right
	
	'''

print binarySearch(a,val)