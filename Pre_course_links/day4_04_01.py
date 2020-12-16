def t1():
    #print('hello')
    return 'hello'
t1()
print()
print(t1(),'\n')

def t1():
    print('hello')
t1()
print(t1())
'''函数末尾默认带上return,当return后面没有跟上东西时，
会默认输出None'''
'''
retrun可以结束整个函数，break只是跳出循环
'''
print()

def t1():
    for i in range(5):
        print(i)
        break
    print('程序结束')

t1()
print()
def t1():
    for i in range(5):
        print(i)
        return#return直接结束函数
    print('程序结束')
t1()

print()
a = 1
def change(a):
    a += 3#由于数值是不可变对象，所以新建了一个变量a
    print(a)
change(a)
print(a)


a = [1,2]
def change(a):
    a.append(3)
    print(a)
change(a)
print(a)
