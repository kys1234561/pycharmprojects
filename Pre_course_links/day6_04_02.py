import os

path1 = r'D:\pycharmProjects\test\test01.txt'

file_path1, file_name1 = os.path.split(path1)
if not os.path.exists(file_path1):
    os.makedirs(file_path1)

file = open(path1,'a')
file.write('\n今天天气不错')
file.close()















import os

path = r'D:\pycharmProjects\test1\text.txt'

file_path, file_name = os.path.split(path)

if not os.path.exists(file_path):
    os.makedirs(file_path)

file = open(path,'w')
file.write('你是最棒的')


