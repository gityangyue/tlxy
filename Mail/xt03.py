#!/usr/bin/python3.6

def process():
    i = 7
    while True:
        i = i + 1
        if i % 2 != 1:
            continue
        if i % 3 != 2:
            continue
        if i % 4 != 3:
            continue
        if i % 5 != 4:
            continue
        if i % 6 != 5:
            continue
        if i % 7 == 0:
            print("该台阶最少有{0}阶".format(i))
            break
if __name__ == "__main__":
    process()
    if 1 < 2 \
    and 2 < 3\
    and 3 < 4\
    and 4 < 5:
        print('成功运行了')

