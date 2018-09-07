#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
第一个数会出现1XN次，第二个数会出现2X(N-1)次，第k个数会出现kX(N-k)次
'''
n = int(input())
l = list(map(float, input().split()))

tot = 0
for i in range(n):
    tot += l[i]*(n-i)*(i+1)

tot = int((tot+0.005)*100)/100
print('{:.2f}'.format(tot))