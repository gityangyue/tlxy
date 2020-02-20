'''
项目分析；
- 构成：
        - 蛇 Snake
        - 食物 Food
        - 世界 Word

- 关系分析：

    思路一：蛇和食物都属于整个世界

        class World:
            self.food
            self.snake
        有点别扭，world无法操作food和snake，代码不太友好。

    思路二：
        食物是一个独立的事物
        蛇是一个独立的事物
        世界是一个独立的事物，负责显示

'''
import queue
import time
import random
import threading
from tkinter import *


class Food():
    '''
    功能：
        1、随机出现在画面上
        2、一旦被吃，则增加蛇的分数
    '''

    def __init__(self, queue):
        '''
        自动产生一个食物
        '''
        self.queue = queue
        self.new_food()

    def new_food(self):
        '''
        功能：产生一个食物
        产生一个食物的过程就是随机产生一个食物坐标的过程
        '''
        #注意坐标产生的范围
        x = random.randrange(5, 490, 10)
        y = random.randrange(5, 290, 10)
        self.position = x, y

        #队列，就是一个不能随意访问内部元素，只能从头弹出一个元素，从队尾追加元素的list
        #把一个食物产生的消息放入队列
        #消息的格式，自己定义
        #定义为：消息是一个dict，k为消息类型，v表示数据

        self.queue.put({'food': self.position})


class World(Tk):
    '''
    用来模拟整个游戏画板

    '''

    def __init__(self,queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False

        #定义画板
        self.canvas = Canvas(self, width=500, height=300, bg='gray')
        self.canvas.pack()

        #画出蛇和食物
        self.snake = self.canvas.create_line((0, 0), (0, 0), fill='black',width=10)
        self.food = self.canvas.create_rectangle(0, 0, 0, 0, fill='#FFCC4C', outline='#FFCC4C')

        self.points_earned = self.canvas.create_text(450, 20, fill='white', text='SCORE:0')

        self.queue_handler()

    def queue_handler(self):
        try:
            #需要不断的从消息队列里拿消息，所以使用死循环
            while True:
                task = self.queue.get(block=False)

                if task.get('game_over'):
                    self.game_over()
                if task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    #重新绘制蛇,食物，分数
                    self.canvas.coords(self.snake, *points)
                if task.get('food'):
                    self.canvas.coords(self.food, *task['food'], *task['food'])
                elif task.get('points_earned'):
                    self.canvas.itemconfigure(self.points_earned, text='SCORE:{}'.format(task['points_earned']))
                    self.queue.task_done()

        except queue.Empty: #爆出队列为空异常
            if not self.is_game_over:
                #after的含义是，在多少毫秒之后调用后面的函数
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        '''
        游戏结束，清理现场
        '''
        self.is_game_over = True
        self.canvas.create_text(200, 150, fill='white', text='Game Over')
        qb = Button(self, text='Quit', command=self.destroy())
        rb = Button(self, text='Again', command=self.__init__)
        self.canvas.create_window(200, 180, anchor='nw', window=qb)


class Snake(threading.Thread):
    '''
    蛇的功能：
        1、蛇能动
        2、蛇每次动，都要重新计算蛇头的位置
        3、检测游戏是否结束
    '''

    def __init__(self, world, queue):
        '''

        '''
        threading.Thread.__init__(self)

        self.world = world
        self.queue = queue
        self.points_earned = 0
        self.food = Food(queue)

        # 描述蛇的各个点,左边保存的是蛇尾，右边保存的是蛇头
        self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]

        self.start()
        #self.daemon = True
        self.direction = 'Left'

    def run(self):
        '''
        一旦启用多线程调用此函数
        要求蛇一直都在跑
        :return:
        '''

        if self.world.is_game_over:
            self._delete()

        while not self.world.is_game_over:
            self.queue.put({'move': self.snake_points})
            time.sleep(0.5)
            self.move()
    def move(self):
        '''
        负责蛇的移动
            1、重新计算蛇头的坐标
            2、当蛇头跟食物相遇，则加分，重新生成食物，通知word，加分
            3、没有相遇，蛇要动
        :return:
        '''
        new_snake_point = self.cal_new_position()

        #当蛇头位置跟食物位置相同
        if self.food.position == new_snake_point:
            self.points_earned += 1 #得分加1
            self.queue.put({'points_earned': self.points_earned})
            self.snake_points.append(self.food.position)
            self.food.new_food()
            self.queue.put({'food': self.food.position})

        else:
            #需要注意蛇的信息的保存方式
            #每次移动是删除存放蛇的最前位置，并在后面追加
            self.snake_points.pop(0)
            #判断程序是否退出，因为新的蛇可能撞墙
            self.check_game_over(new_snake_point)
            self.snake_points.append(new_snake_point)

    def cal_new_position(self):
        '''
        计算新的蛇头的位置
        '''
        last_x, last_y = self.snake_points[-1]
        if self.direction == 'Up':  # direction 负责蛇移动的方向
            new_snake_point = last_x, last_y - 10 #每次移动是10个像素
        elif self.direction == 'Down':
            new_snake_point = last_x, last_y + 10
        elif self.direction == 'Left':
            new_snake_point = last_x - 10, last_y
        elif self.direction == 'Right':
            new_snake_point = last_x + 10, last_y
        return new_snake_point

    def key_pressed(self,event):
        #keysym是按键名称
        self.direction = event.keysym


    def check_game_over(self, snake_point):
        '''
        判断的依据是蛇头是否和墙相撞
        就是把蛇头的坐标拿出来，跟墙的坐标进行匹配
        '''

        x, y = snake_point[0], snake_point[1]
        if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
            self.queue.put({'game_over':True})


def main():
    q = queue.Queue()
    world = World(q)
    world.title('媳妇要做饭之贪吃蛇')
    snake = Snake(world, q)
    #绑定方向键
    world.bind('<Key-Left>', snake.key_pressed)
    world.bind('<Key-Right>', snake.key_pressed)
    world.bind('<Key-Up>', snake.key_pressed)
    world.bind('<Key-Down>', snake.key_pressed)

    world.mainloop()


if __name__ == '__main__':
    main()
