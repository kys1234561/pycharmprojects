if True:
    a = 6
print(a)

print()

total1 = 2

def add(args1,args2):
    total = args1+args2
    print(total1)

add(5,4)
print(total1)
print()

total = 0

def add(args1,args2):
    total = args1+args2
    print(total)

add(5,4)
print(total)

print()

total = 0
print(id(total))
def add(args1,args2):
    total = args1+args2
    print(id(total))
    return total

print(add(5,4))
total=add(5,4)
print(total)


print()

total = 0
print(id(total))
def add(args1,args2):
    global total
    total = args1+args2
    print(id(total))
    return total

print(add(5,4))
print(total)
print(id(total))


print()
'''
total = 0
print(id(total))
def add(total,args1,args2):
    total = total
    total = args1+args2
    print(id(total))
    return total

print(add(total,5,4))
print(id(total))
print(total)
'''