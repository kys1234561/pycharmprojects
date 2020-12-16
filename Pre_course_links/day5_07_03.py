class car:
    def __init__(self):#self不是关键字,在类下面写方法，一定要参数（对象），
        #python默认使用self(最好使用默认的),也可以用其他的名字，比如a,b,c等等，此处实现创建对象功能
        self.color = '白色'
        self.name = '特斯拉'
        self.speed = '450km/h'

    def run(self):
        print('车跑起来了，颜色：{0}，名字：{1}，速度：{2}'.format(self.color,self.name,self.speed))

c1 = car()
c1.run()

c1.color = '黑色'
c1.run()