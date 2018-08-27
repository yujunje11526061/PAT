#!/usr/bin/env.python
# -*- coding:utf-8 -*-
nc = int(input())
lc = sorted(map(int, input().split()), reverse = True)
np = int(input())
lp = sorted(map(int, input().split()), reverse = True)

def cal():
    i, i = 0, 0
    total = 0
    while i<nc and i<np and lc[i]>0 and lp[i]>0:
        total += lc[i]*lp[i]
        i += 1
    if i ==nc or i==np:
        return total
    elif lc[i] <= 0 or lp[i]<=0:
        j = -1
        while j >= -nc and j >= -np and lc[j] <0 and lp[j]<0:
            total += lc[j]*lp[j]
            j -= 1
    return total


print(cal())
