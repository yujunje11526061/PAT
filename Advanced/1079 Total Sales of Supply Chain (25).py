#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import deque
n, unit, r = input().split()
n, unit, r = int(n), float(unit), float(r)
chain = [None]*n
if n==1:
    num, *seq = map(int, input().split())
    print('0.0')
else:
    ret = set()
    for i in range(n):
        num, *seq = map(int,input().split())
        chain[i] =seq
        if num == 0:
            ret.add(i)

    tot = 0
    q = deque([[0, unit]])
    while len(q)>0:
        i, price = q.popleft()
        price *= (r/100+1)
        for j in chain[i]:
            if j in ret:
                tot += chain[j][0]*price
                continue
            q.append([j,price])

    print('{:.1f}'.format(tot))
