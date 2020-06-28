#!/usr/bin/env python
# -*- coding:utf-8 -*-
n, d = map(int, input().split())

l = []
for i in range(n):
    loc, num = map(int, input().split())
    l.append((loc, num))

l.sort()

def find(s,e):
    if l[e][0]-l[s][0]<d:
        return s
    while l[e][0]-l[s][0]>=d:
        s += 1
    return s-1

if len(l) <= 1 or l[-1][0] - l[0][0] < d:
    print(0)
else:
    maxSum = [None] * n
    maxSum[0] = 0
    # maxSum表示到下标i为止，前面的最大和是多少
    # 故由dp知：maxSum[i] = max(maxSum[i-1], l[i][1]+ max_money_of_legal_position_j_before_i
    # 慢就慢在max_money_and_legal_position_j_before_i怎么求，往前扫描则复杂度为O（d），总的O（n^2）。
    # 考虑到距离是有序的，另外存一个数组，记录到i为止的钱最多的银行的金钱量
    maxMoney = [None]*n # 必然非减，从而最多往前搜索d次，一旦距离合格，就可以直接取到前面钱最多的银行的钱。
    maxMoney[0] = l[0][1]
    for i in range(1,n):
        maxMoney[i] = l[i][1] if l[i][1]>maxMoney[i-1] else maxMoney[i-1]

    s = 0
    for i in range(1,n):
        j = find(s,i) # 不需要二分，直接在上次结束的位置（距离必然合法）开始往后扫描应该更快，因为通常不需要d次
        maxSum[i] = max(maxSum[i-1], l[i][1]+maxMoney[j])
        s = j
    print(maxSum[-1])

# 6 3
# 1 1
# 3 5
# 4 8
# 6 4
# 10 3
# 11 2
#
