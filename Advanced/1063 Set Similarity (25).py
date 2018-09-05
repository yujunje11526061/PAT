#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N = int(input())
ts = [None]
for i in range(1,N+1):
    ss = map(int, input().split())
    num = next(ss)
    ts.append(set(ss))

K = int(input())
for _ in range(K):
    i,j = map(int, input().split())
    tot = ts[i] | ts[j]
    si = ts[i] & ts[j]
    print('{:.1f}%'.format(len(si)/len(tot)*100))