#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
l = sorted(map(int, input().split()))
if n == 2:
    print(sum(l)//2)
else:
    tot = l[0]
    for i in l[1:]:
        tot = (tot+i)/2

    print(int(tot))
