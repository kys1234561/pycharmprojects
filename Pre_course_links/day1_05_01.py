a = 8
b = bin(a)
c = oct(a)
print(b)
print(c,'\n')

f = int(c, 8)
print(f,'\n')
f = int('0x35', 16)
print(f,'\n')
f = int('100',10)
print(f,'\n')

d = 17
e = hex(d)
print(e)