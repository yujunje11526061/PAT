#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
两个优先队列，一个管理人，一个管理窗口，权值分别为到达时间和可以提供服务的时间，两队同步弹出一个，计算时间差。
'''

import heapq

N, K = map(int, input().split())

def cal(t:str):
    hh, mm, ss = map(int, t.split(":"))
    return hh*3600+mm*60+ss

start = cal('08:00:00')
# end = cal("17:00:00")

heap = []
for i in range(N):
    at, pt = input().split()
    if at>'17:00:00':
        continue
    heapq.heappush(heap, (cal(at), int(pt)*60) )

n = len(heap)
total = 0
W = [start for i in range(K)] # 管理各个窗口的优先队列，权值为可以服务的时间

for i in range(n):
    p = heapq.heappop(heap)
    ava = heapq.heappop(W) # 获得下一个有窗口可以服务的的时间
    if p[0] < ava:
        total += (ava-p[0])
        ava += p[1]
    else:  # 不用排队的情况
        ava = p[0]+p[1]

    heapq.heappush(W, ava)

total = total/60/n
print('{:.1f}'.format(total))


