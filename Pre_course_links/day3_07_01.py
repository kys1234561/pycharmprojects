for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}  '.format(j,i,i*j),end='')
    print()
print()
a = 0
while a <= 10:
    if a != 8:
        print(a,end=' ')
    a += 1
    if a == 8:
        continue
print()
a = 0
while a <= 10:
    if a == 8:
        a += 1
        continue
    print(a,end=' ')
    a += 1

print()

#chr表示将数字转化成字符，
for i in range(97,97+26):
    print(chr(i),end=' ')
print()
a ='jack james'
print(a.upper())
print(a.capitalize())
print(a.title())

a ='jack JJJJames'
print(a.lower())

alist =[1,5,2,6,9,3]
print(sorted(alist),'\n')
print(alist,'\n')
alist.sort()
print(alist)

'''alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
print(sorted(alist))'''