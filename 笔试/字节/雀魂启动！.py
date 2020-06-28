#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import defaultdict
l = map(int, input().split())

d = defaultdict(lambda :0)

for i in l:
    d[i] += 1


def insert0(i):
    while d[i]==0 and i<10:
        i += 1

    if i==10:
        return True

    flag = False
    if d[i]<3:
        if d[i+1]==0 or d[i+2]==0:
            flag =  False
        else:
            d[i] -= 1
            d[i+1] -=1
            d[i+2] -= 1
            flag = insert0(i)
            d[i] += 1
            d[i + 1] += 1
            d[i + 2] += 1
    else:
        if d[i+1]>0 and d[i+2]>0:
            d[i] -= 1
            d[i+1] -=1
            d[i+2] -= 1
            flag = insert0(i)
            d[i] += 1
            d[i + 1] += 1
            d[i + 2] += 1
        if flag:
            return True
        d[i] -= 3
        flag = insert0(i)
        d[i] += 3

    return flag


def insert(n):
    for i in range(1,10):
        if d[i]>1:
            d[i] -= 2
            if insert0(0):
                d[i] += 2
                return True
            d[i] += 2

    return False




result = []
for n in range(1,10):
    if d[n]==4:
        continue

    d[n] += 1
    if insert(n):
        result.append(n)
    d[n] -= 1

if len(result):
    print(*result)
else:
    print(0)