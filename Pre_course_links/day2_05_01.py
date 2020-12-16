students = ['张三','李四','王五']
s1 = ['第一','第二','第三']
print(students)
students.append('赵六')
print(students[3])
print(students)
students.extend(s1)
print(students)
students.insert(1,'新内容')
print(students)
students.insert(2,'李九')
print(students)
students[1] = '那可'
print(students)

del students[1]
print(students)
students.insert(1,'新内容')
print(students)

students.pop(3)
print(students)
students.remove('赵六')
print(students)