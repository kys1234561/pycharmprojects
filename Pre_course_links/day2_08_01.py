s1 = set('saopwjl')
s2 = set('efdgdsa')
print(s1)
print(s2)
print(s1 - s2)
print(s1 | s2)
print(s1 & s2)
print(s1 ^ s2)

#集合存放的是键(keys)，不存放值(values),存在映射关系，必要时通过键来对集合进行操作

s3 = set([1,2,3])
print(s3)
s3.add(5635)
print(s3)
s3.update([3,6,8,9,0])
print(s3)
s3.remove(0)
print(s3)
print(len(s3))

s4 = {1,2,3,4,5,7,8,9,}
print((s4))
print(type(s4))

'''
dict1 = {'身高：':175,'体重：':65}
print(dict1)
print(dict1['身高：'])
'''