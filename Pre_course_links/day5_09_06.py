class person:

    def __init__(self):
        self.age = 0

    def pr(self):
        print('你的年龄是：', self.age)

    def change(self, age):
        if age <0 or age > 120:
            print('年龄不合法')
        else:
            self.age = age

p1 = person()
p1.change(90)
p1.pr()
