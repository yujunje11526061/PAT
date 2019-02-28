#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
math库的使用，数学思想，递推
'''

from math import log10, floor

n = int(input())
total = 0

while n>0:
    k = floor(log10(n)) # n为k+1位数
    # 先求到最大的k位数总共有多少(包括位数不足k位的)，用递推公式
    sk = 0
    for i in range(k):
        sk = 10*sk + 10**i

    total += sk
    # 截止这里，到最大的k位数时，总共多少1已经统计出来了

    a, b = divmod(n, 10**k)
    if a > 1: # 说明以1开头的那一套k位数全在范围内，# (a-1)套尾巴的k位数，10**k个头
        total += (a-1)*sk + 10**k  # 这里a-1时防止之前已经统计了的那部分k位数被重复计算
    else: # 说明以1开头的那一套k位数只有一部分在范围内，数目为 余数+1.
        total += b+1
    # 截止这里，k位数都统计了，k+1位数中有几套k位数和几个头也统计了，把n替换为剩下的不满一套k位数的部分
    n = b

print(total)
from collections import deque