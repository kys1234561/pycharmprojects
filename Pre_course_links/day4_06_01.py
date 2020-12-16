def add(a,*b):
    print(a)
    print(b)
    print(type(b))
    sum = a
    for s in b:
        sum += s
    print(sum)

add(1,2,3,4,5,6)

def d(name,age=0):
    print('姓名：',name)#多个输出之间用逗号隔开
    print('年龄：',age)

d('张三')

print(3,4)


print()
def add1(a,*b):
    sum = a
    for i in b:
        sum += i
    print(sum)

add1(3,2,4,5,6,3)


def s1(name,age=30):
    print('名字：',name)
    print('年龄：',age)
s1('王六')