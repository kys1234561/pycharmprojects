import requests
from bs4 import BeautifulSoup

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0"}
re = requests.get('https://book.douban.com/subject/4913064/comments/',headers = headers,verify=False).text
re1 = BeautifulSoup(re,features='lxml')

pater = re1.find_all('span','short')
print(pater)
print('------------------------------------------------')
for i in pater:
    print('\n',i.get_text())