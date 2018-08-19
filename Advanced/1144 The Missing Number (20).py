#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
l = sorted(map(int, input().split()))
try:
    i = l.index(1)
    l = l[i + 1:]
    flag = 1
    for j in l:
        if j - flag <= 1:
            flag = j
        else:
            break
    print(flag + 1)
except:
    print(1)
