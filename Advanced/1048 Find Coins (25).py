#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
字典统计每种币的个数
无重复的最小堆弹出拥有的最小币种，避免单独对面值排序
循环执行到目标额度的一半即可
找加和因子到一半，找乘积因子到平方根
'''
import heapq as hq
N, M = map(int, input().split())
s = map(int, input().split())
d= {}
heap = []
for i in s:
    if d.get(i,0) == 0:
        d[i] =  1
        heap.append(i)
    else:
        d[i] += 1

hq.heapify(heap)
# print(d)
e = hq.heappop(heap)
while e <= M/2:
    r = M-e
    if r==e and d[e]>1:
        print(e, r)
        break
    if r != e and  d.get(r,0) > 0:
        print(e,r)
        break
    e = hq.heappop(heap)

if e>M/2:
    print('No Solution')
