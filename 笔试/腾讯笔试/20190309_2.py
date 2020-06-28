#!/usr/bin/env python
# -*- coding:utf-8 -*-

q = int(input())

for i in range(q):
    tot = 0
    l, r = map(int, input().split())
    lx, rx = l * ((-1) ** l), r * ((-1) ** r)
    cnt = r - l + 1
    if lx > 0:
        tot = - (cnt // 2)
    else:
        tot = cnt // 2
    if cnt%2==1:
        tot += rx

    print(tot)
