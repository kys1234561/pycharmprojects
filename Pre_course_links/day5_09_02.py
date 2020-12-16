class A:
    a = 1
    def pr(self):
        print('A')

class B(A):
    a = 3
    def pr(self):
        print('B')

class C(B):
    a = 3
    def pr(self):
        print('C')

c = C()
'''c.pr1()
c.pr2()
c.pr3()'''
c.pr()