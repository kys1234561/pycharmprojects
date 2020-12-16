class A:
    def __init__(self):
        self.name = '张三'
        self.age = 23

    def pr(self):
        print(self.name)
        print(self.age)

class B(A):
    def __init__(self, sex):
        super().__init__()
        self.sex = sex

    def pr(self):
        super().pr()
        print(self.sex)


a = B('男')
a.pr()
