import tkinter
import random
import threading
import time

# 初始化窗口
root = tkinter.Tk()
root.title("抽取奖品")
root.geometry('500x800+400+200')
root.resizable(False, False)
root.flag = True





#生成奖池
'''
list1 = ['焖烧杯' for i in range(8)]
list2 = ['饭盒' for i in range(4)]
list3 = ['毛驴' for i in range(4)]
list4 = ['化妆镜' for i in range(3)]
list5 = ['充电宝' for i in range(5)]
list6 = ['加湿器' for i in range(5)]
list7 = ['大杯子' for i in range(4)]
list8 = ['小杯子', '小杯子']
list9 = ['手机支架' for i in range(4)]
list10 = ['宿舍锅' for i in range(5)]
list11 = ['榨汁杯' for i in range(8)]
list12 = ['坚果', '坚果']
'''
quanty = {'坚果': 2,
          '焖烧杯': 8,
          '饭盒': 4,
          '毛驴': 4,
          '化妆镜': 3,
          '充电宝': 5,
          '加湿器': 5,
          '大杯子': 4,
          '小杯子': 2,
          '手机支架': 4,
          '宿舍锅': 5,
          '榨汁杯': 8
}
students = ['坚果', '焖烧杯', '饭盒', '毛驴', '化妆镜', '充电宝', '加湿器', '大杯子' ,'小杯子' ,'手机支架', '宿舍锅','榨汁杯']

# 三个Lable标签
num = 0
first = tkinter.Label(root, text='', font=("宋体", 20, "normal"))
first.place(x=180, y=100, width=150, height=100)

second = tkinter.Label(root, text='已抽奖人数{0}'.format(num), font=("宋体", 20, "normal"))
second['fg'] = 'red'
second.place(x=180, y=200, width=200, height=100)

third = tkinter.Label(root, text='', font=("宋体", 10, "normal"), wraplength=500)
third.place(x=10, y=300, width=500, height=500)
def switch():
    root.flag = True
    while root.flag :
#    while len(students) != 0:
        i = random.randint(0, len(students) - 1)

        first['text'] = students[i]

        #print(students[i])
        #print(students)
        #print(quanty)

        #print(num)
       # first['text'] = second['text']
        #second['text'] = third['text']
        #third['text'] = students[i]
        time.sleep(0.1)




# 开始按钮
def butStartClick():
    t = threading.Thread(target=switch)
    t.start()
    butStop.config(state='active')


btnStart = tkinter.Button(root, text='开始', command=butStartClick)
btnStart.place(x=30, y=30, width=80, height=20)


# 结束按钮
def btnStopClick():
    global num
    root.flag = False
    quanty[first['text']] -= 1
    if quanty[first['text']] < 1:
        students.remove(first['text'])

    num += 1
    second['text'] = '已抽奖人数{0}'.format(num)
    # 显示当前奖池的奖品
    a = '目前奖池的奖品为：\n'
    for j in quanty.keys():
        a = a + str(j) + str(quanty[j]) + '\n' + '\n'
    third['text'] = a
    butStop.config(state='disabled')


butStop = tkinter.Button(root, text='停止', command=btnStopClick, state='disabled')
butStop.place(x=160, y=30, width=80, height=20)

# 启动主程序
root.mainloop()
#switch()