class person:
    def __init__(self):
        self.age = 0
    def pr(self):
        print('你的年龄是：', self.age)

p1 = person()
p1.age = 90
p1.pr()


print()


class person:
    def __init__(self):
        self.__age = 0#在age前面加两横就是私有变量
    def pr(self):
        print('你的年龄是：', self.__age)

p1 = person()
p1.__age = 90
p1.pr()


print()



#以下的方法不要使用，不方便
class person:
    def __init__(self, age):
        self.__age = age
    def pr(self):
        print('你的年龄是：', self.__age)

p1 = person(90)
p1.pr()