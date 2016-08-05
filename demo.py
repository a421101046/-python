# -- coding: utf-8 --

step = raw_input("请输入一个的布长>")

target = 25
dis = 0.001
step = float(step)
start = 0
count = 0

while abs(start ** 2 - target) > dis  and start <= target:
	start += step
	count += 1
	
if (start <= target):
	print "success"
else:
	print "fail"
	
print "循环次数:%d"  %count 
