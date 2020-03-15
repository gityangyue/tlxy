import tkinter



if __name__ == '__main__':
    root_window =tkinter.Tk()

    root_window.title('飞机大战')
    root_window.resizable(width=False, height=False)


    #创建画布
    window_cavas = tkinter.Canvas(root_window, width=480, height=680)
    window_cavas.pack()

    #在画布上画一个图片
    #三个步骤：
    #1 定义图片位置
    #2 创建photoImage对象
    #3利用Creat——image函数把图片画上去

    bg_img_name = '../img/background.gif'
    bg_img = tkinter.PhotoImage(file=bg_img_name)
    #tags的作用是，以后我嗯使用创建好的image可以通过tags使用
    window_cavas.create_image(240, 300, anchor=tkinter.CENTER,
                              image=bg_img, tags='bg')

    #画上一个小蜜蜂
    bee_img_name = '../img/bee.gif'
    bee_img = tkinter.PhotoImage(file=bee_img_name)
    # tags的作用是，以后我嗯使用创建好的image可以通过tags使用
    window_cavas.create_image(240, 300, anchor=tkinter.CENTER,
                              image=bee_img, tags='bee')


    root_window.mainloop()