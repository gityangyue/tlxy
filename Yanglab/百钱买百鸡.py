'''
百钱买百鸡
1、鸡翁5钱
2、鸡母3钱
3、三只鸡雏一钱
求100钱怎么买100只鸡
'''
qty = list()
qty1 = dict()
slt = 0
for i in range(19):
    for j in range(30):
        for k in range(300):
            sum = i*5 + j*3 + k/3
            if sum == 100 and i+k+j == 100:
                qty.append("鸡翁：{0}, 鸡母：{1}, 鸡雏：{2}".format(i, j, k))
               # qty1[i] = "鸡翁：{0}, 鸡母：{1}, 鸡雏：{2}".format(i, j, k)

print(qty)
print(qty1)