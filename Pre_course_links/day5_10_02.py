class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('姓名：{0}, 年龄： {1}'.format(self.name,self.age))

a = A('张三',34)

