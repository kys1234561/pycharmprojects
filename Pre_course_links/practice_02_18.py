class Student(object):
    def __init__(self, name, sex, age, home_address):
        self.name = name
        self.sex = sex
        self.age = age
        self.home_address = home_address

    def display(self):
        print('名字：{0}，性别：{1}，年龄：{2}，家庭住址：{3}'.format(self.name,
                                                     self.sex,self.age,self.home_address))


me = Student('柯友盛','男',23,'成都信息工程大学')
me.display()


















print()
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def dis_paly(self):
        print(self.name)


c = Cat('小花',3)
c.dis_paly()



