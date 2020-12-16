class animal:
    def eat(self):
        print('吃')

class dog(animal):
    def bark(self):
        print('汪汪汪')

class border(dog):
    def character(self):
        print('忠诚，温和')

bor1 = border()
bor1.eat()
bor1.bark()
bor1.character()