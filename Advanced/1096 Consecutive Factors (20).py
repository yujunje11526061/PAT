#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
20分题一般不考太多算法，考审题和考虑全不全面。
看似n很大，实际扫描代价很小。上限由n一开平方后直接没多少了，连乘几下就除完了，不整除直接跳出了。
'''
import math

n = int(input())

maxl = 0
maxf = int(math.sqrt(n)) + 1
start = 0
for i in range(2, maxf): # 连乘的因子上限肯定不超过这个，恰好开平方连乘长度也才1，所以扫描起点只要在这之间就好了
    temp = n
    start_ = i
    count = 0
    for j in range(i, maxf): # 从每个起点往后扫
        if temp % j != 0: # 不能被整除就可以跳出了，连乘到此为止
            break
        temp = temp//j
        count += 1
    if count > maxl:  # 因为是从小的开始扫描，所以只有连乘数更大时才更新。
        maxl = count
        start = start_


if start == 0: # 没有启动过，说明时质数，输出自己
    print(1)
    print(n)
elif maxl == 1 and start !=0: # 启动了但是最大长度是1，说明是平方数
    print(1)
    print(start)
else:
    print(maxl)
    s = '*'.join(['{}'] * maxl)
    seq = [i for i in range(start, start+maxl+1)]
    print(s.format(*seq))
