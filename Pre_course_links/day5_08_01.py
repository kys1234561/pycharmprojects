class person:

    def __init__(self, name):#习惯用self来表示当前的实例
        self.name = name

    def cry(self):
        print(self.name, '哭了')

p1 = person('张三')
p1.cry()

