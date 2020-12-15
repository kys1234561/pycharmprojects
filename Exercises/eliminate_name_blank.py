name = '    \n   Albert  Einst  \n  \t'
print(name)
print(str.lstrip(name))#lstrip是字符串下面的方法，所以要带上str。。。str.lstrip是将字符串左边的空格去除，
# 同时将所有非必要的字符（比如此处的Albert  Einst是必要字符）去除。
print(str.rstrip(name))
print(str.strip(name))