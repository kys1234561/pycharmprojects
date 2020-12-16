'''
num_list = [1,5,2,3,9]
num_list.sort()
print(num_list)

num_list = [1,5,2,3,9]
print(sorted(num_list))
print(num_list)
num_list.reverse()#reverse本身的意思有反向，reverse表示反向排序
print(num_list)

num_list = []
l1 = [1,2,3]
print(num_list)
num_list.append(l1)
print(num_list)
'''
num_list = []
l1 = [1,2,3]
l2 = [4,5,6]
l1.append(l2)
print(l1,'\n')
num_list.append(l1)
print(num_list)
num_list.append(l1)
print(num_list)
#num_list[0][3][1] = 100
#print(num_list)
print(num_list[0][3][2])
print(num_list[1][3][2])



a = [[1,2,3],[53,2,1]]
print(a[0][1])

a = [1,2,3]
b = [1,4,8]
a.extend(b)
print(a)
a.extend(b)
print(a)

a = [1,2,3]
b = [1,4,8]
a.append(b)
print(a)
print(a[0])
print(a[3])
print(a[3][1])
a.append(b)
print(a)
print(a[0])
print(a[3])
print(a[3][1])


a = [1]
a.insert(1,3)
print(a)
a.remove(1)
print(a)

a = [1]
a.insert(1,3)
print(a)
a.pop(1)
print(a)
