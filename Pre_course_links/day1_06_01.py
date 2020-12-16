a = '的粉色闪电'
print(a)

a = "水电费双方都"
print(a,'\n')

a = '''敷设敷设吧
十多个
神鼎飞丹砂'''
print(a,'\n')


a = """dfdsfs
nvbn
gfgd
4355"""
print(a)

b = "''"
print(b)
c = '""'
print(c)

print("‘3’比‘2’大")



a = 6
b = 7
#print('{}+{}={3}'.format(a,b,a*b,a+b))#会报错，不能从自动字段编号切换到手动字段规范
print('{}+{}={}'.format(a,b,a+b),'\n')
print('{0}+{1}={3}'.format(a,b,a*b,a+b))
print('{0}-{1}={3}'.format(a,b,a*b,a-b))

a = 6
b = 7
print('{0}*{1}={3}'.format(a,b,a+b,a*b))

print('2\n6')
print(type('2\n5'))

#print(type('2'))