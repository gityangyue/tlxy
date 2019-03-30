# 写一个程序，打印出0~100所有的奇数
def jishu():
    for i in range(101):
        if i % 2 == 1:
            print(i,end=" ")

if __name__ == "__main__":
    print('0~100所有的奇数为：')
    jishu()