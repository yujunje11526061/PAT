#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq
N, start = input().split()
N = int(N)

l = [None] * 100000

for i in range(N):
    loc, *info = map(int, input().split())
    l[loc] = info

flag = 0
ll = []
p = int(start)
if p == -1 or l[p] is None:
    flag = 1
else:
    while p != -1:
        ll.append([int(l[p][0]), p])
        p = l[p][1]

heapq.heapify(ll)
if flag == 1:
    print(0, start)
else:
    # ll.sort()
    print('{} {:0>5}'.format(len(ll), ll[0][1]))
    for i in range(len(ll) - 1):
        item = heapq.heappop(ll)
        print('{:0>5} {} {:0>5}'.format(item[1], item[0], ll[0][1]))

    print('{:0>5} {} {}'.format(ll[0][1], ll[0][0], -1))
