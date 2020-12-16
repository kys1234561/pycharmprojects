a = 3

def t1():
    global a
    a = 4
    print(a)
t1()
print(a)
print()

def outer():
    a = 4
    def inner():
        nonlocal  a#在闭包中用nonlocal
        a = 7
        print(a)
    inner()
    print(a)

outer()


print()

list1 = [24,6,7,2,7,8,3]

for i,j in enumerate(list1):
    print(i,'-----',j)

print()


