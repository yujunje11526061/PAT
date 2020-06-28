#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input())

price = []
for i in range(n):
    price.append(list(map(int, input().split())))

visited = [0]*n

minPrice = 0x7fffffff

def dfs(now,tot,count):
    global minPrice
    if count==n:
        tot += price[now][0]
        minPrice = tot if tot<minPrice else minPrice

    for i in range(n):
        if visited[i]:
            continue
        else:
            visited[i] = 1
            dfs(i, tot+price[now][i],count+1)
            visited[i] = 0



visited[0] =  1
dfs(0,0,1)
visited[0] =  0

print(minPrice)