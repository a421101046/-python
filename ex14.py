# -- coding: utf-8 --

from sys import argv 

script , user_name , password = argv

prompt = ' > '

print "你好%s, 我是%s脚本" % ( user_name , script)

print "我能问你些问题么 ?"

print "你喜欢干什么? %s" %( user_name )

likes = raw_input(prompt)

print "你住哪? %s " %(user_name)

lives = raw_input(prompt)

print "你喜欢哪种电脑? %s " %(user_name)

computer = raw_input(prompt)


print """

你喜欢%s ,
你住在%s ,
你喜欢%s电脑

""" %(likes , lives, computer)

print "记住密码 %s" % (password)