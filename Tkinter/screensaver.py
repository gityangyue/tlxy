'''
项目名称 ：屏保
项目分析：
    1 屏保可以自己启动，也可以手动启动
    2 一旦敲击键盘或者移动鼠标，或者其他的引发事件，则停止
    3 如果屏保是一幅画的话，则没有画框
    4 图像的动作是随机的，具有随机性，可能包括颜色，大小，多少，运动方向，变形等

程序设计

    1 Screensaver：
        a 需要一个canvas，大小与屏幕大小一致， 没有边框


    2 Ball
        a 颜色，大小，多少，运动方向，变形等随机
        b 球能动，可以被调用

'''

import random
import tkinter

class RandomBall():
    #定义运动的球的类
    def __init__(self, canvas, scrnwidth, scrnheight):

        # canvas:画布，所有的内容都应该在画布上呈现。此处通过该参数传入
        # scrnwidth、scrnhigh：屏幕宽高
        self.canvas = canvas

        #球出现的初始位置，随机定义
        # xpos ：X坐标
        # ypos ： Y坐标
        self.xpos = random.randint(200, int(scrnwidth)-200)
        self.ypos = random.randint(200, int(scrnheight)-200)

        #定义球运动的速度
        #模拟运动：不断的擦掉原来的球，然后在一个新的地方再绘制
        #此处xvelocity，yvelocity 模拟x轴，y轴的运动
        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)

        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        # 球的大小随机,radius表示球的半径
        self.radius = random.randint(20, 120)

        #定义颜色
        #RGB：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        #在某些系统中可以用英文单词表示颜色，比如：red，green
        #这里用lambda表达式
        color = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x'%(color(), color(), color())

    def creat_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        # Tkinter没有画圆形的函数
        #只有一个画椭圆的函数，画椭圆需要定义两个坐标
        #在另一个长方形内画椭圆，我们只需要定义长方形左上角和右下角的坐标
        #求两个坐标的方法是，一直圆心的坐标，圆心坐标减去半径就是左上角，加上半径就是右下角。

        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        #在有两个对角坐标的前提下，可以进行画圆
        #fill表示填充颜色
        #outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, \
                                           fill=self.color, \
                                           outline=self.color)

    def move_ball(self):
        #移动球的时候，需要控制球的方向
        #每次移动后，球都有一个新的坐标，
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        #以下判断球是否到画布的边界，如果到边界则反向运动
        #注意撞墙的算法判断。
        if self.xpos + self.radius >= self.scrnwidth:
            #到了右边界
            self.xvelocity = -self.xvelocity

        if self.ypos + self.radius >= self.scrnheight:
            # 到了下边界
            self.yvelocity = -self.yvelocity

        if self.ypos - self.radius <= 0:
            #到了上边界
            self.yvelocity = -self.yvelocity

        if self.xpos - self.radius <= 0:
            #到了左边界
            self.xvelocity = -self.xvelocity

        #在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)

class ScreenSaver():
    #定义屏保的类
    #可以被启动

    #用列表装随机产生的球
    balls = list()

    def __init__(self):
        #每次启动球的数量随机
        self.num_balls = random.randint(6, 20)
        #self.num_balls = 1

        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)

        #任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        #同理，安东任何键盘都需要退出屏保
        self.root.bind('<Key>', self.myquit)
        #得到屏幕大小规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        #在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.creat_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        #after是200毫秒后启动一个函数，需要启动的函数是第二个参数,不是python递归的实现，不会在10000次递归之后停止。
        self.canvas.after(50, self.run_screen_saver)

    def myquit(self, event):
        #利用事件处理机制
        #实际上不关心事件的类型
        self.root.destroy()

if __name__ == "__main__":

    #启动屏保
    ScreenSaver()