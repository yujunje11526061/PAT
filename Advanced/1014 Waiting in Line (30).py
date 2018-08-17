#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
建立两个优先队列，每个窗口都没满时，以人数为主指标，每个窗口都满时，以最早空闲时间(窗口队首那个人的服务结束时间)，副指标都是窗口编号
'''

import heapq as hp
from collections import deque
N, M, K, Q  = map(int, input().split())
t = list(map(int, input().split()))
P = map(int, input().split())

class Window():
    def __init__(self, i):
        self.id = i
        self.num = 0
        self.time = 0
        self.ttime = 0
        self.line = deque()

    @property
    def x(self):
        return [self.num, self.id]
    @property
    def y(self):
        return [self.time, self.id]

W = [Window(i) for i in range(N)]

wd = [[w.x, w] for w in W] # w.x包含队伍数， 窗口号
hp.heapify(wd)

s = {0:0} # 记录每人的服务开始时间
d = {} # 记录每人的理论服务结束时间

for k in range(K):
    elem = wd[0][-1] # 以窗口排队人数为首要指标的最小堆，取得人数最少且编号最小的窗口
    if elem.num < M: # 各个窗口都没满
        elem.num += 1
        elem.ttime += t[k]
        d[k] = elem.ttime

        s[k] = d[elem.line[-1]] if len(elem.line)>0 else 0 # 队伍中前一人的结束时间就是我的开始时间
        elem.line.append(k)

        wd[0][0] = elem.x
        hp.heapify(wd)

    else:  # 各个窗口都满了，此时要进队一人就要出队一人，建以下次空闲时间为首要指标的最小堆
        for w in W:
            w.time = d[w.line[0]]
        wt = [[w.y, w] for w in W]  # w.y 包含下次空闲时间， 窗口号
        hp.heapify(wt)
        elem = wt[0][-1]
        elem.line.popleft()
        elem.ttime += t[k]
        d[k] = elem.ttime

        s[k] = d[elem.line[-1]]
        elem.line.append(k)

# for those customers who cannot be served before 17:00, you must output "Sorry" instead.
# 从5：00前就已经开始服务的，虽然最终的服务时间超过五点，也不是Sorry，而只有从五点之后才会被开始服务的，会是Sorry。这个很关键，不然会有答案错误的案例。
def cal(p):
    h,m = divmod(d[p], 60)
    h += 8
    hstart,mstart = divmod(s[p], 60)
    hstart += 8
    if hstart>=17:
        return 'Sorry'
    return '{:0>2}:{:0>2}'.format(h,m)

for p in P:
    print(cal(p-1))