#!/usr/bin/env.python
# -*- coding:utf-8 -*-

# 浮点数精度问题真是python一个大问题，放弃

line1 = input().split()
line2 = input().split()

num1 = int(line1[0])
num2 = int(line2[0])

line1 = line1[1:]
line2 = line2[1:]

l1 = []
l2 = []

for i in range(len(line1)//2):
    l1.append((int(line1[2*i]), float(line1[2*i+1])))

for i in range(len(line2)//2):
    l2.append((int(line2[2 * i]), float(line2[2 * i + 1])))

# print(l1, l2)

def mul(t1,t2):
    return [t1[0]+t2[0], t1[1]*t2[1]]

ll = [mul(i,j) for i in l1 for j in l2]
ll.sort(key = lambda i:i[0], reverse = True)
# print(ll)

fl = []
init = list(ll[0])
item = False
for item in ll[1:]:
    if init[0] == item[0]:
        init[1] = init[1]+item[1]
    else:
        if abs(init[1]) >= 0.05:
            fl.append(init)
        init = list(item)
# print(fl)
if item is not False:
    fl.append(init)

n = len(fl)
print(n, end = '')
for k in fl:
    # # print(k[1])
    # coeint, coe = '{:.3f}'.format(k[1]).split('.')
    # coe = int(coe)
    # # 本题计算得到的结果最多为两位小数，python浮点数精度是近似表示的，精度控制很难，受整数位长度影响，故直接取小数部分分析,最后用字符串保存
    # if coe%100//10 >= 5:
    #     k[1] = coeint + '.' + str(coe//100+1)
    # else:
    #     k[1] = coeint + '.' +str(coe//100)
    # # print(k[1])
    print(' {} {}'.format(k[0], round(k[1],1)), end= "")
