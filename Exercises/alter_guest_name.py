name = ['张三', '李四', '王文', '赵文']
for inter in name:
    print(inter,'邀请你来共进晚餐')
print('张三','不能来赴约')

name[inter == '张三'] = '李九'

print()

for inter in name:
    print(inter,'邀请你来共进晚餐')