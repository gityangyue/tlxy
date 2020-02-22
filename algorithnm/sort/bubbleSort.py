#冒泡排序
#依次将最大的数移动到列表末尾。
import random


def bubbleSort_simple(li):
    for i in range(len(li)-1): # 第n次冒泡
        exchange = False              # 标识交换
        for j in range(len(li)-i-1):  # 将无序区的最大值放入有序区
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        print(li)
        if not exchange:                   # 如果没有进行交换表明已全部有序，排序结束
            break


    return li


li = [random.randint(0,1000) for k in range(10)]
print(li)
print(bubbleSort_simple(li))

