#!/usr/local/bin/python3.6

#自己写的代码
def sxhs(number):
    number = int(number)
    baiwei = number // 100
    #print(baiwei)
    shiwei = ( number % 100 ) // 10
    #print(shiwei)
    gewei = number % 10
    #print(gewei)
    sum = (baiwei * baiwei * baiwei) + (shiwei * shiwei * shiwei) + (gewei * gewei * gewei)
    if sum == number:
        return sum
    else:
        return None

if __name__ == "__main__":
    print('100到1000之间的水仙花数为：')
    for i in range(100, 1000):
        rst = sxhs(i)
        if rst != None:
            print(rst)


# 更好的代码

def sxhs(number):
    tmp = list(str(number))
    a = int(tmp[0])
    b = int(tmp[1])
    c = int(tmp[2])
    sum = a**3 + b**3 + c**3
    if sum == int(number):
        return sum
    else:
        return None

if __name__ == "__main__":
    print('100到1000之间的水仙花数为：')
    for i in range(100, 1000):
        rst = sxhs(i)
        if rst != None:
            print(rst)