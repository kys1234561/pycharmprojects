a = 5
b = 6
print(a & b)
print(a | b)
print(a ^ b)
print(a ^ b ^b)

a = a ^ b
print(a)
b = a ^ b
print(b)
a = a ^ b
print('a = {}, b = {}'.format(a,b))