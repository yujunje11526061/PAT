#!/usr/bin/env.python
# -*- coding:utf-8 -*-
l = list(map(int, input().split()))
N, l = l[0], l[1:]

way = [0]*N
# way = [0]*N
for i in range(N-1):
    way[i+1] = l[i] + way[i]

total = way[-1]+l[-1]
# print(way)
K = int(input())
for _ in range(K):
    i,j = map(int, input().split())
    i,j = i-1,j-1
    if i>j:
        i,j = j,i
    x = way[j]-way[i]
    y = total-x
    print(min(x,y))
