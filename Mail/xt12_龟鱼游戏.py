'''
假设游戏场景范围（x,y）为0<=x<=10 , 0<=y<=10
游戏生成一个乌龟和10条鱼
他们的移动方向均随机
乌龟的最大移动能力是2（乌龟可以随机选择移动是1还是2），鱼的最大移动能力是1
当移动到场景边缘，自动反向移动
乌龟的初始体力为100(上限)
乌龟每移动一次，体力消耗1
当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力加20
鱼不计算体力
当乌龟体力值为0或者鱼的数量为0时，游戏结束

'''

import random as r

class Turtle(object):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        self.power = 100

    def move(self):
        new_x = r.choice([-2, -1, 1, 2]) + self.x
        new_y = r.choice([-2, -1, 1, 2]) + self.y

        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.power -= 1
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish(object):
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = r.choice([-1, 1]) + self.x
        new_y = r.choice([-1, 1]) + self.y

        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)

turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完了，游戏结束")
        print("乌龟还有{}体力".format(turtle.power))
        break
    if not turtle.power:
        print("乌龟体力耗尽了，游戏结束")
        print("剩下的鱼为：" + str(fish))
        break
    turtle_pos = turtle.move()
    for each_fish in fish[:]:
        if each_fish.move() == turtle_pos:
            turtle.eat()
            fish.remove(each_fish)
            print("鱼{}被吃掉了".format(each_fish))
            print("乌龟的体力为{}".format(turtle.power))


