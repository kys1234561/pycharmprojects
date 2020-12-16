class person:

    def eat(self):
        print('吃饭')

    def speak(self):
        print('说话')

class student(person):
    def study(self):
        print('学习')


p1 = person()
p1.eat()
p1.speak()
print()
student1 = student()
student1.eat()
student1.speak()
student1.study()