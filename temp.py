# -- coding: utf-8 --

# 原版
# left = 0
# right = 100
# mid = left / 2 + right / 2
# print "Is your secret number %d?" % mid 
# msg = ""
# 
# while(True):
# 	char = raw_input(msg)
# 	if char == "h":					# 高了
# 		right = (left + right) / 2 
# 		mid = left / 2 + right / 2
# 		msg = "你的数是" + str(mid) + " ? "
# 	elif char == "l":				# 低了
# 		left = (left + right) / 2 
# 		mid = left / 2 + right / 2
# 		msg = "你的数是" + str(mid) + " ? "
# 	elif char == "c":				# 正确
# 		print("谢谢你的参与")
# 		break
# 	else :
# 		print "你输入的有问题"
# 		msg = "请重新输入"
# 	
# 	


# 修正版
left = 0
right = 100
guessed = False

while(not guessed):
	guess = (left  + right) /  2
	print "你的数是 %d?"  % guess 

	char = raw_input('>')
	if char == "h":					# 高了
		right = guess
	elif char == "l":				# 低了
		left = guess
	elif char == "c":				# 正确
		print("谢谢你的参与")
		guessed = True
	else :
		print "你输入的有问题"

22
		
# 写代码 注意 true 不要写成 True   敲符号的时候注意 输入法
