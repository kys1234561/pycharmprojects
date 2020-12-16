s1 = 'dsadsfadfad'
#序列一定是从左到右查找
print(s1[4 : 9])
print(s1[4 : 8])
print(s1)
print(s1[ : ])
print(s1[ : len(s1)],'\n')
print(s1[-1 : 3])#序列一定是从左到右查找,此处输出为空
print(s1[ : -1])

s2 = 'dfasdf'
print(s1+s2)#+在此处代表字符串连接符
print(s2*2)#*在此处代表字符串连接符,*后面一定是数字