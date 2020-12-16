class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #print('姓名：{0}, 年龄： {1}'.format(self.name,self.age))

    def __str__(self):#此处是对类的专有方法进行重写
        return '姓名：{0}, 年龄： {1}'.format(self.name,self.age)
a = student('张三',34)
print(a)
