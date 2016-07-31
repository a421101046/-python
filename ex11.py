# -- coding: utf-8 --

print "你几岁呀" , 

age = raw_input()

print "你多高啊" ,

height = raw_input()

print "你多重呀" ,

weight = raw_input()

print "你现今%r岁 ,你有%r高 ,你有%r重 "  % (age , height ,weight)


# 在每行 加了个逗号 ,这样print输出就不跑到下一行了。

# raw_input() 把每个输入数据,都当成字符串返回 (可以接受任何类型的输入,包括表达式)
# 并且会把字符串多余的' "进行转义


