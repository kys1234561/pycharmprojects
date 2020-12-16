class dictclass:
    def __init__(self, dict1):
        self.dict1 = dict1
        print(self.dict1)

    def del_dict(self, key0):
        self.key0 = key0
        del self.dict1[self.key0]
        print(self.dict1)

    def get_dict(self, s1):
        if s1 in self.dict1:
            print(self.dict1[s1])
        else:
            print('not found')

    def get_key(self):
        list1 = []
        for i in self.dict1:
            list1.append(i)
        print(list1)


    def update_dict(self,new_dict):
        self.new_dict = new_dict
        self.dict1.update(new_dict)
        print(self.dict1)


d1 = dictclass({'姓名':'张三','年龄':34,'性别':'男'})
print()
d1.del_dict('姓名')
d1.get_dict('年龄')
d1.get_key()
d1.update_dict({'年薪':100000,'学历':'本科'})