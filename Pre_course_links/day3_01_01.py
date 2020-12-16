a,b = 3,4
print(a,b)
a,b = (3,4)
print(a,b)
(a,b) = (3,4)
print(a,b)
[a,b] = (3,4)
print(a,b)
[a,b] = [3,4]
print(a,b)
a,b = b,a
print(a,b)
print(type(a))
print(type(b))

a,b = '3' '4'
print(a,b)
print(type(a))
print(type(b))
a,b,c = '你好呀'
print(a,b,c,'\n')


a,b,*c = '你好呀!'
print(a,b,c)

a,b,*c = '1,2,3,4,4,5,6'
print(a,b,c)
a,b,*c = '1 2,3,4,4,5,6'
print(a,b,c)

a,*b,c = '你好吗？'
print(a,b,c)

a,b,*c = '你好吗？'#最多只有一个未知长度的列表，即最多只有一个星号
print(a,b,c)

a = b = c = d = 90
print(a,b,c,d)
a = 1000
print(a,b,c,d)

a = 90
b = a
c = a
d = a
print(a,b,c,d)
b = 1000
print(a,b,c,d)
