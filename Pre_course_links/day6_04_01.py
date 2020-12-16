path = 'test.txt'

file = open(path,'w')
file.write('python是一门语言')
file.close()
file = open(path,'a')
file.write('\npython是一门语言')
file.close()
file = open(path,'r')
str = file.read()
print(str)
file.close()

print(r'\'')