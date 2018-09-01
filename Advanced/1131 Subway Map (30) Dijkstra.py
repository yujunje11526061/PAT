#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
直接dfs，当存在环时非常麻烦，找到最短路过程中，环中有些部分相当于经过了了很多次。非常耗时。
得把visited，path等很多参数反复传参并新建副本，耗时耗内存。递归程序也不好调试。
应该先按各权值均为1的最短路径问题，用Dijkstra算法初筛一次，记录最短路径，然后回溯。
回溯过程相当于一个有向图，无环，计算量一下子小很多。
最好先Dijkstra， 但由于中间站点不唯一，故统计所有等长路径后得再BFS。
'''
import heapq as hq
from collections import deque

N = int(input())
table = [[] for i in range(10000)]
which = {}
for line in range(1, N + 1):
    n, *sta = map(int, input().split())
    for i in range(n - 1):
        table[sta[i]].append(sta[i + 1])
        table[sta[i + 1]].append(sta[i])
        x = which.setdefault(sta[i], set())
        x.add(line)
    x = which.setdefault(sta[n - 1], set())
    x.add(line)


def Dijkstra(s, e):
    visited = [0] * 10000
    inf = float('inf')
    path = [[] for i in range(10000)]
    dist = [inf] * 10000
    dist[s] = 0
    h = [[dist[s], s]]  # 距离起点的距离， i的编号
    while len(h) > 0:
        _, i = hq.heappop(h)
        if visited[i]:
            continue
        if i == e:
            return path
        visited[i] = 1
        for j in table[i]:
            if visited[j]:
                continue
            if dist[j] > dist[i] + 1:
                dist[j] = dist[i] + 1
                path[j] = [i]
                hq.heappush(h, [dist[j], j])
            elif dist[j] == dist[i] + 1:
                path[j].append(i)


qn = int(input())
for _ in range(qn):
    start, end = map(int, input().split())
    path = Dijkstra(start, end)
    q = deque([(end, [end], None, 0)])
    tot = float('inf')
    while len(q) > 0:  # BFS回溯的过程, 不能用visited，应该把所有路径回溯出来再比，反正有向图不会绕圈
        now, r, line1, t = q.popleft()
        for i in path[now]:
            flag = 0
            line2 = (which[now] & which[i]).pop()
            if line1 != line2 and line1 is not None:
                flag = 1
            q.append((i, r + [i], line2, t + flag))
        if now == start and  t < tot:
            tot = t
            way = r

    print(len(way)-1)
    every_start = start
    pp = start
    line1 = None
    for p in way[-2::-1]:
        line2 = (which[pp] & which[p]).pop()
        if line2 != line1 and pp != start:
            print('Take Line#{} from {:0>4} to {:0>4}.'.format(line1, every_start, pp))
            every_start = pp
        line1 = line2
        pp = p
    print('Take Line#{} from {:0>4} to {:0>4}.'.format(line1, every_start, pp))
