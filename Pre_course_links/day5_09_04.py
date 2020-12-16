class A:

    def pr(self):
        print('A')

    def __init__(self, name):
        self.name = name
        print(self.name)

class C(A):
    a = 3

    def __init__(self, name):
        super().__init__(name)

c = C('张三')
'''c.pr1()
c.pr2()
c.pr3()'''




#gfhg//hg..f/h
print()
class A:

    def pr(self):
        print('A')

    def __init__(self, name):
        self.name = name
        print(self.name)

class C(A):
    a = 3
    def pr(self):
        print('C')
    def __init__(self, name):
        super().__init__(name)

c = C('张三')