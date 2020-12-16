def recursive(h):
    f = [0] * 100
    f[0] = 0
    f[1] = f[2] = 1
    if h == 1:
        print(f[0])
    elif h == 2 or h == 3:
        print(f[1])
    else:
        for i in range(3,h+1):
            f[i] = f[i-1] + f[i-2]
        print(f[h-1])
recursive(10)



print()
def recursive1(h):
    f = [0] * (h+1)
    f[0] = 1
    f[1] = 2
    for i in range(2,h+1):
        f[i] = f[i-1] + f[i-2]
    print(f)
    sum = 0
    for j in range(0,h):
        sum += f[j+1] / f[j]
    print(sum)

recursive1(20)




print()


def recursive2(h):
    f = [0] * (h+2)
    f[0] = f[1] =  1
    for i in range(2,h+2):
        f[i] = f[i-1] + f[i-2]
    print(f)
    sum = 0
    for j in range(1,h+1):
        sum += f[j+1] / f[j]
    print(sum)





recursive2(20)
print()

a = 1
b = 2
s = 0
for i in range(20):
    s += b / a
    t = a + b
    a = b
    b = t
print(s)