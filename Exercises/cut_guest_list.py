name = ['张三', '李四', '王文', '赵文']
name.insert(0,'王一')#对象.方法(位置，元素)
name.insert(len(name)//2,'李九')
name.append('季真')
for inter in name:
    print(inter,'邀请你来共进晚餐')
print('只能邀请两位嘉宾来共进晚餐')
print('\n')
'''for i in range(len(name)-2):
    print(name[i],'抱歉不能邀请你来共进晚餐')
print()
for i in range(len(name)-2):
    name.pop(0)
print()'''
len1 = len(name)
for i in range(len1-2):
    print(name[0],'抱歉不能邀请你来共进晚餐')
    name.pop(0)
print()

for i in range(len(name)):
    print(name[i],'你依然在受邀之列')
print()
del name[0]
del name[0]
print(name)