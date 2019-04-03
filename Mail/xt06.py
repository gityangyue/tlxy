#!/urs/local/bin/python3.6

#类似于排列组合的编程，可以用for 循环列举全部，将符合要求的输出即可
#有红，黄，蓝 三种颜色的球，红球3个，黄球3个，蓝球6个，将这12个
#球放入一个盒子中，从中任意取出8个球，编程计算摸出球的各种颜色搭配xt0 6.py

def sanseqiu():
    csq = 0
    for red in range(2):
        for yellow in range(2):
            for blue in range(2,9):
                if 8 == red + yellow + blue:
                    csq += 1
                    print('''
                        第{0}种方案：
                            红球 ： {1}
                            黄球 ： {2}
                            蓝球 ： {3}                        
                        '''.format(csq, red, yellow, blue))
if __name__ == '__main__':
    sanseqiu()