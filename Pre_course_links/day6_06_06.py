import json

data = (1,2,3,4,5)

with open('data1.json','w') as f:
    json.dump(data, f)
    #dump()方法将python格式转成json格式


with open('data1.json','r') as f:
    data1 = json.load(f)
    #load将json格式转化成python格式

print(data1)
print(type(data1))

