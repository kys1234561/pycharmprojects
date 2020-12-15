way = ['New York','Nan Jing','Bei Jing','Dong Jing','Shang Hai']
way1 = sorted(way)
print(way1)

way1 = sorted(way,reverse=True)
print(way1)

way1.reverse()
print(way1)

way1.sort()
print(way1)

way.insert(0,'Cheng Du')
print(way)
way.append('Wu Han')
print(way)
del way[0]
print(way)