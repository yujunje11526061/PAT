#!/usr/bin/env.python
# -*- coding:utf-8 -*-

import heapq
N = int(input())
d = []
num = 0
for i in range(1, N + 1):
    location_number = i
    K = int(input())
    l = []
    num += K
    for j in range(K):
        id, score = map(int, input().split())
        l.append([score, -id, i])
    l.sort(reverse=True)
    cnt = l[0][0]
    rank = 1
    for x in range(len(l)):
        if l[x][0] == cnt:
            l[x].append(rank)
        else:
            rank = x + 1
            cnt = l[x][0]
            l[x].append(rank)

    d.append(l)

d = heapq.merge(*d, reverse=True)
print(num)
cnt = 101
rank = 0
x = 0
for elem in d:
    if elem[0] == cnt:
        elem.append(rank)
        x += 1
    else:
        rank = x + 1
        cnt = elem[0]
        elem.append(rank)
        x += 1
    s = '{} {} {} {}'.format(-elem[1], elem[-1], elem[2], elem[3])
    print(s)
