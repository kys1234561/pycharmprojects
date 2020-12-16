import re

str = 't4og runs to car\\'
print(re.search(r'car\\',str))
print(re.search(r't\dog',str))
print()








print(re.search(r'\d',str))#此处rS起到抑制转义的作用
print(re.search(r't\dog',str))
print(re.search(r'\D',str))
print(re.search(r'\s',str))
print(re.search(r'\S',str))

print()

str = '''
dog runs to car.
I run to dog.'''
print(re.search(r'I',str,flags=re.MULTILINE))



