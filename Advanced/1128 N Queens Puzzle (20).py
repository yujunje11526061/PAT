#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())

def judge():
    for i in range(num):
        x = seq[i]
        for j in range(i+1, num):
            y = seq[j]
            if abs(y-x)==abs(j-i):
                return 'NO'
    return 'YES'

for i in range(n):
    num, *seq = map(int, input().split())
    ss = set(seq)
    if len(ss) != num:
        print('NO')
    else:
        print(judge())
