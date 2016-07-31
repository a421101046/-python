# -- coding: utf-8 -- 

formatter = "%r %r %r %r";
formatter1 = "%s %s %s %s";

print formatter % (1, 2, 3, 4)

print formatter1 % ("一", "二", "三", "四")
# print formatter % ("一", "二", "三", "四")

print formatter % (formatter, formatter, formatter, formatter)


print formatter % (
	"I had this thing" , 
	"That you could type up right ",
	"But it didn't sing ",
	"So I said goodnight"
)


# 错误 1.变量名写错了  2. %r 不能打印中文字符
