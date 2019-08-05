#递归函数
def digui(num):
    print(num)
    if num > 0:
        digui(num-1)
    else:
        print("=" * 20)
    print(num)

#digui(3)
steps = int(0)
def hanota(num, a, b, c):
    global steps
    if 1 == num:
        steps += 1
        print("第{0}次操作：".format(steps) + a + " ----->" + c)
    if num >= 2:
        hanota(num-1,a, c, b)
        hanota(1, a, b, c)
        hanota(num-1, b, a, c)
    if num < 1:
        print("你疯了，哪有负数的")
hanota(5, "A", "B", "C")
print("最少需要{0}次".format(steps))

