''''
判断一个数是否是质数
'''


class IsZhiShu(object):
    def __init__(self, n):
        self.num = int(n)
        self.result = False
        if n == 1 or n ==2:
            print("该数是质数")
        if n < 1 :
            print("闹呢，这个肯定不是质数")

    def method1(self):
        for i in range(2, self.num):
            if self.num % i == 0:
                break
            else:
                    self.result = True
        return self.result

    def method2(self):
        for i in range(2, int(self.num/2)):
            if self.num % i == 0:
                break
            else:
                self.result = True
        return self.result

    def method3(self):
        for i in range(2, int(self.num**0.5)):
            if self.num % i == 0:
                break
            else:
                self.result = True
        return self.result


class IsZhiYinShu(object):
    def __init__(self, n):
        self.num = int(n)
        self.flag = False
        self.result = []
        self.i = 2
    def filter(self):
        while self.i < self.num:
            if self.num % self.i == 0:
                self.num = (self.num // self.i)
                self.result.append(self.i)
            else:
                self.i += 1
        print(self.result,self.i)
        return self.num


a = IsZhiYinShu(100)
print(a.filter())





