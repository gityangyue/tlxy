'''
- 模拟系统的计算器功能
- 实现一个简单的具有加减法等操作的计算器
- 使用tkinter
设计思路：
    - 画GUI
    - 给每个控件配置相应的事件
    - 写逻辑代码

'''


#第一步：画出图形界面
from tkinter import *


root = Tk()
#定义面板的大小
root.geometry('250x380')
root.title('北京图灵学院')

#定义面板
#bg代表背景颜色，（background），#dddddd是十六进制表示颜色的代码
frame_show = Frame(width=600, height=300, bg='#dddddd')


#定义顶部区域
sv = StringVar()
sv.set('0')

#定义计算器的显示屏
#anchor:定义控件的锚点，e代表东，即右边
#font 代表字体
show_lablel = Label(frame_show, textvariable=sv,
                    bg='green', width=12, height=1,
                    font=('黑体', 20, 'bold'),
                    justify=LEFT, anchor='e')
show_lablel.pack(padx=10, pady=10)
frame_show.pack()

#逻辑代码
'''
考虑以下几种情况
1 按下数字
2 按下操作符号
3 只考虑两个操作数的操作，不考虑复杂情况
'''

num1 = ''
num2 = ''
operator = None
rst = ''
def delete():
    global operator, num1, num2
    if operator:
        num2 = list(num2)
        num2.pop()
        print(num2)
        num2 = ''.join(num2)
        sv.set(num1+operator+num2)
    else:
        num1 = list(num1)
        num1.pop()
        num1 = ''.join(num1)
        print(num1)
        sv.set(num1)


def fan():
    pass


def clear():
    global num1, num2
    sv.set('0')
    num1 = ''
    num2 = ''
    operator = None

def change(num):
    '''
    按下一个数字需要考虑两种情况：
    1 数字属于第一个操作数
    2 数字属于第二个操作数
    3 判断是否属于第一个操作数，可以通过operator 来判断

    '''
    global num1, num2, operator

    #假如操作数是None，表明肯定是第一个操作数
    if not operator:
        num1 = num1 + num
        #如果是第一个操作数，则只显示第一个操作数
        sv.set(num1)
    else:
        num2 = num2 + num
        #如果是第二个操作数，则应该显示完整的计算式
        sv.set(num1+operator+num2)



def operation(op):
    global rst, operator
    if op in ['+', '-', 'x', '/']:
        operator = op
        sv.set(str(num1)+operator)
    if op == "=":    #认为按下的是等于号
        if operator == "+":
            rst = float(num1) + float(num2)
        if operator == "-":
                rst = float(num1) - float(num2)
        if operator == "x":
            rst = float(num1) * float(num2)
        if operator == "/":
            rst = float(num1) / float(num2)
        sv.set(str(rst))
        operator = None
#定义按键区域
frame_board = Frame(width=400, height=350, bg='#cccccc')

#定义按键
b_delete = Button(frame_board, text='←', width=5, height=1, command=delete)
b_delete.grid(row=0, column=0)
b_delete = Button(frame_board, text='C', width=5, height=1, command=clear)
b_delete.grid(row=0, column=1)
b_delete = Button(frame_board, text='±', width=5, height=1, command=fan)
b_delete.grid(row=0, column=2)
b_delete = Button(frame_board, text='CE', width=5, height=1, command=clear)
b_delete.grid(row=0, column=3)

#定义数字键1-0 ， 这里用lambda函数可以避免定义类似功能的10个数字按键的函数
b_1 = Button(frame_board, text='1', width=5, height=2, command=lambda: change('1')).grid(row=1, column=0)
b_2 = Button(frame_board, text='2', width=5, height=2, command=lambda: change('2')).grid(row=1, column=1)
b_3 = Button(frame_board, text='3', width=5, height=2, command=lambda: change('3')).grid(row=1, column=2)
b_4 = Button(frame_board, text='4', width=5, height=2, command=lambda: change('4')).grid(row=2, column=0)
b_5 = Button(frame_board, text='5', width=5, height=2, command=lambda: change('5')).grid(row=2, column=1)
b_6 = Button(frame_board, text='6', width=5, height=2, command=lambda: change('6')).grid(row=2, column=2)
b_7 = Button(frame_board, text='7', width=5, height=2, command=lambda: change('7')).grid(row=3, column=0)
b_8 = Button(frame_board, text='8', width=5, height=2, command=lambda: change('8')).grid(row=3, column=1)
b_9 = Button(frame_board, text='9', width=5, height=2, command=lambda: change('9')).grid(row=3, column=2)
b_0 = Button(frame_board, text='0', width=5, height=2, command=lambda: change('0')).grid(row=4, column=1)
b_dot = Button(frame_board, text='.', width=5, height=2, command=lambda: change('.')).grid(row=4, column=2)

#定义运算按键
b_jia = Button(frame_board, text='+', width=5, height=2, command=lambda: operation('+')).grid(row=1, column=3)
b_jian = Button(frame_board, text='-', width=5, height=2, command=lambda: operation('-')).grid(row=2, column=3)
b_cheng = Button(frame_board, text='x', width=5, height=2, command=lambda: operation('x')).grid(row=3, column=3)
b_chu = Button(frame_board, text='/', width=5, height=2, command=lambda: operation('/')).grid(row=4, column=0)
b_rst = Button(frame_board, text='=', width=5, height=2, command=lambda: operation('=')).grid(row=4, column=3)
frame_board.pack()



root.mainloop()