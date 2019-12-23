''''
定义一个门票系统
门票的原价是100元
当周末的时候门票涨价20%
小孩子半价票
计算两个成人和一个小孩的平日票价
'''


class Ticket(object):
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1

        if child:
            self.decrease = 0.5
        else:
            self.decrease = 1

    def cal_price(self, num):
        return self.price * self.increase * self.decrease * num


adult = Ticket()
child = Ticket(child=True)
print("两个成年人和一个小孩子的平日票价为{0}".format(adult.cal_price(2)+child.cal_price(1)))