class student:
    def __init__(self, age, scores):
        self.age = age
        self.scores = scores

    def get_name(self,name):
        self.name = name
        print(self.name)
    def get_age(self):
        print(self.age)

    def get_course(self):
        print(max(self.scores))

zm = student(20,[69,88,100])
zm.get_name('张三')
'''zm.get_age()
zm.get_course()
#zm.get_name()



print()

class student1:
    def __init__(self, name, age, Chinese, Math, English):
        self.name = name
        self.age = age
        self.Chinese = Chinese
        self.Math = Math
        self.English = English

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)

    def get_course(self):
        print(max([self.Chinese,self.Math,self.English]))

zm = student1('zhangming',20,69,88,100)
zm.get_name()
zm.get_age()
zm.get_course()
#zm.get_name()
'''


d1 = {'姓名':'张三','年龄':34}
print(len(d1))

a = 'a:43|b:45'
c = a.split('|')
print(a)
d = {}
e = []
for i in c:
    key, value = i.split(':')
    d[key] = value
    e = e+list(key)
print(e)
print(d)
for i in d:
    print(i)

for i in c:
    print(i)