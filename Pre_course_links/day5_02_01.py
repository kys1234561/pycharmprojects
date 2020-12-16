str1 = 'string'
print(str1)
str2 = reversed(str1)  # 此时str2表示的是在某个位置反转对象
print(str2)
print(list(str2))
print(id(str2))

print(len(str1))
for i in range(len(str1) - 1, -1, -1):
    print(str1[i], end='')
print()

name = 'jack james'
up_name = name.upper()
print(up_name)
low_name = up_name.lower()
print(low_name)
initial_name = name.title()
print(initial_name)

print('Lao tze said:"A journey of a thousand miles begins with the first step"')
name = 'Lao tze'
quote = '"A journey of a thousand miles begins with the first step"'
print(name, 'said:', quote)

name = '   Lao\ntz\te   '
quote = '"A journey of a thousand miles begins with the first step"'
print(name, 'said:', quote)
print()
name1 = name.strip()
name2 = name.lstrip()
name3 = name.rstrip()
print(name1)
print(name2)
print(name3)

list1 = [2, 3, 7, -34, 21, -4, 0.65]
for i in range(len(list1)):
    if list1[i] < 0:
        list1[i] = abs(list1[i])

print(list1)

alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
for i in range(len(alist) - 1):
    for j in range(i + 1, len(alist)):
        if alist[i]['age'] < alist[j]['age']:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp
print(alist)
print(alist[0]['age'])

str = 'k:1|k1:2|k2:3|k3:4'
str1 = str.split('|')
print(str1)
list1 = []
for i in str1:
    list1 += i.split(':')
print(list1)
dict1 = {}
dict2 = {}
for i in range(0, len(list1), 2):
    dict1.update({list1[i]: list1[i + 1]})
    dict2[list1[i]] = list1[i + 1]
    print({list1[i]: list1[i + 1]})
print(dict1)
print('nice')
print(dict2)
print()

list1 = [1, 2, 3, 4]
list2 = ['dfsd,’dfs']
print(list1 + list2)
list1.extend(list2)
print(list1)

list1 = [1, 2, -5, 2, 4, -90, -43]
list1.sort(key=abs)
print(list1)
