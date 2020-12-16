#from  urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0"}
#html = urlopen('https://book.douban.com/subject/4913064/comments/',headers  = headers)\
   #.read().decode('utf_8')
html = requests.get('https://book.douban.com/subject/4913064/comments/',headers  = headers,verify=False).text
#print(html)
re1=BeautifulSoup(html,'lxml')#lxml是BeautifulSoup对于html的常用解析器,用来解析源代码
#print(re1)
print('___________________________________________________')
pattern=re1.find_all('span','short')
'''
count=0
for item in pattern:
    count=count+1
    print(count,item.string)'''
print(pattern)
print('___________________________________________________')
for i in pattern:
    print('\n',i.get_text())

