# 写一个程序，判断一个年份是否为闰年
def isrnian(year):
    year = int(year)
    if year % 4 == 0:
        print("这是闰年")
    else:
        print("这不是闰年")

year = input("请输入一个年份：")
if year.isdigit():
    isrnian(year)
else:
    print("您输入的不是数字")
print("*" * 50)

# 给用户三次机会，猜想我们程序生成的一个数字，每次用户猜想过后会提示数字是否正确，以及用户输入的数字大于，还是小于。当机会用完后提示用户已经输掉了游戏
def game(number):
    global a
    if a == number:
        print("恭喜你，猜对了")
        return 1
    if a < number:
        print("您猜的数字大了")
    if a > number:
        print("您猜的数字小了")

import random
a = random.randint(1,100)

#print(a)
print("游戏开始...............")


for i in range(3):
    numbe = input("请输入您想的数字:")
    if numbe.isdigit():
        numbe = int(numbe)
        rst = game(numbe)
        if rst == 1:
            break
    else:
        print("您输入的不是数字，浪费了一次机会，请输入数字")
    if i == 2:
        print("游戏结束，您输了")
        print("这个数字是{0}".format(a))