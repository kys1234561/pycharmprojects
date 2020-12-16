'''class A:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def educational_background(self, ed):
        self.ed= ed

    def pr(self):
        print('他的名字是：',self.name)
        print('他的年龄是：', self.age)
        print('他的学历是：', self.ed)
class B(A):

    def educational_background(self, ed):
        self.ed = ed



b = B('张三',32,'男')
b.educational_background('本科')
b.pr()
print()
b.educational_background('研究生')
b.pr()

print()
'''

class A:

    def __init__(self):#self表示实例对象，实例对象才有方法
        self.name = '张三'
        self.age = 34
        self.sex = '男'


    def pr(self):
        print('他的名字是：',self.name)
        print('他的年龄是：', self.age)
        print('他的性别是：', self.sex)



class C:

    def __init__(self):#self表示实例对象，实例对象才有方法
        self.name = '李四'
        self.age = 38
        self.sex = '男'


    def pr(self):
        print('他的名字是：',self.name)
        print('他的年龄是：', self.age)
        print('他的性别是：', self.sex)


class B(C,A):

    def __init__(self,salary):
        super().__init__()
        #super()直接进入实例对象中
        # 重写了父类方法，使用super函数可以实现该父类方法的初始值被子类继承
        self.salary = salary


    def pr(self):
        super().pr()#super()函数实现该父类方法的初始值被子类继承
        print('他工资的是：',self.salary)


b = B(9000)
b.pr()
print()
