def make_album(name,album):
    print({album:name})

make_album('周杰伦','稻香')
make_album('李荣浩','麻雀')
make_album('薛之谦','天外来物')


def make_album(name,album,len=''):
    print({album:name})
make_album('周杰伦','稻香',1)

print('!!!!!!!!!!!!!!!!!!!!!!!!!!1')
#下面是一次添加多个形参
def add(*a):#可以传入多个形参
    print({"a":4,"b":3,"c":4})
add()

def add(a, *f):#可以传入多个值
    print(a,f)
add(4)
add(4, 5)
add(5, 7, 3)


def add(*a):
    print(a)
add(5)
add(4, 6)
add(5, 7, 6)

