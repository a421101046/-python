# -- coding:utf-8 --
# 接受参数的脚本 解包 变量

# “import”  引入python的sys引入进来 , sys叫模组即modules,又称库即libraries
# argv是一个参数的变量 , 包含你传递给python的参数
from sys import argv

# 对argv进行解包 unpack , 接受 >=3 个参数  必须用argv
script, first, second, third = argv

print "The script is called:" , script

print "You first variable is:" , first

print "You second variable is:" , second

print "You third variable is:" , third


# 在命令行中要执行 python ex13.py  [参数] [参数] [参数]

