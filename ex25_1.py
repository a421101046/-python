# --coding: utf-8--


from ex25 import * # 导入ex25文件中所有的变量

sentence = "All goods things come to those who wait"

# 分割句子中的单词
words = break_words(sentence)

print(words)

# 数组中单词排序
print(sort_words(words))

# 打印第一个单词
print_first_word(words)

# 打印最后一个单词
print_last_word(words)

# 打印变量
print(num)




"""
在shell中如何导入别的.py文件
1. 输入python,进入命令行
2. import ex25
3. ex25.break_words(\"I like you\")


三引号之间为帮助文档

help(ex25) 可以显示函数的内容

"""



