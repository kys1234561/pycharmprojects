import time


print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%y-%m-%d %H:%M:%S',time.localtime()))
print(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))

print(time.time())
print(time.localtime())

a = 'Wed Nov 11 11:26:54 2020'
print()
print(a)
print(time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y')))
#将格式字符串转化为时间戳