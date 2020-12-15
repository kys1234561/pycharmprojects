name = ['张三', '李四', '王文', '赵文']
for inter in name:
    print(inter, '邀请你来共进晚餐')
print()
name.insert(0,'王一')#对象.方法(位置，元素)
name.insert(len(name)//2,'李九')
name.append('季真')
for inter in name:
    print(inter,'邀请你来共进晚餐')
print('\n')