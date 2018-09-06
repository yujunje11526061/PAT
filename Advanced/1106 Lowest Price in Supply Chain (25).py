#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import deque
n, unit,r =input().strip().split()
n = int(n)
unit, r = float(unit), float(r)

table = [0 for i in range(n)]
for i in range(n):
    seq = map(int, input().strip().split())
    num = next(seq)
    if num>0:
        table[i] = list(seq)

if n==1:
    print('{:.4f} {}'.format(unit, 1))
else:
    q = deque([[0,0]])
    tc = 1000000000000
    count = 0
    while len(q)>0:
        this, cnt = q.popleft()
        if table[this] == 0:
            if cnt<=tc:
                tc = cnt
                count += 1
                continue
            else:
                break
        cnt += 1
        for j in table[this]:
            q.append([j, cnt])

    price = int(unit * ((100 + r)/100) ** tc*10000+0.5)/10000
    print('{:.4f} {}'.format(price, count))