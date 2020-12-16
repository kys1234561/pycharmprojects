class car:
    color = '白色'
    name = '特斯拉'
    speed = '450km/h'

    def run(self):
        print('车跑起来了，颜色：{0}，名字：{1}，速度：{2}'.format(self.color, self.name, self.speed))
c1 = car()
c1.run()
c1.color = '黑色'
c1.run()
c2 = car()
c2.run()

car.color = '黄色'
c2.run()
c1.run()
c1 = car()
c1.run()