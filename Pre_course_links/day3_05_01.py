a = 100
while a <= 999:
    a1 = a % 10
    a2 = a // 10 % 10
    a3 = a // 100
    if a1 ** 3 + a2 ** 3 + a3 ** 3 == a:
        print(a)
    a += 1

a = [1,2,3,4,5]
i = len(a)-1
while i >= 1:
    print(a[i],end=',')
    i -= 1
    if i == 0:
        print(a[i])
print('\n')

a = [1,2,3,4,5,8]
i = len(a)
j = -1
while j >= -i+1:
    print(a[j],end=',')
    j -= 1
    if j == -i:
        print(a[j],'\n')


num = 1357924680
while num > 0:
    a = num % 10
    print(a,end='')
    num = num // 10


