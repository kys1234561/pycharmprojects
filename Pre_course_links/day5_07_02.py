class car:
    def init(self):
        self.color = '白色'
        self.name = '特斯拉'
        self.speed = '450km/h'

    def run(self):
        print('车跑起来了，颜色：{0}，名字：{1}，速度：{2}'.format(self.color,self.name,self.speed))

c1 = car()
c1.init()
c1.run()




c1.color = '黑色'
c1.run()