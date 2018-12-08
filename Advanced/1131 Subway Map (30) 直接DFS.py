#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
直接dfs，当存在环时非常麻烦，找到最短路过程中，环中有些部分相当于经过了了很多次。非常耗时。
得把visited，path等很多参数反复传参并新建副本，耗时耗内存。递归程序也不好调试。
应该先按各权值均为1的最短路径问题，用Dijkstra算法初筛一次，记录最短路径，然后回溯。
回溯过程相当于一个有向图，无环，计算量一下子小很多。
最好Dijkstra， 但由于中间站点不唯一，故统计所有路径后得再DFS。
'''
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



def dfs(s, e, xl, count, trs, line, vi):
    global length, least,path, tr_in_path
    ll = list(xl)
    visited = list(vi)
    if s == e:
        ll.append(e)
        if len(ll) < length or (len(ll) == length and count < least):
            length = len(ll)
            least = count
            path = ll
            tr_in_path = trs
        return
    visited[s] = 1
    ll.append(s)
    for i in table[s]:
        if visited[i]:
            continue
        count_ = count
        tr = set(trs)
        newline = (which[s] & which[i]).pop()
        if newline != line and s != start:
            count_ += 1
            tr.add(s)
        dfs(i, e, ll, count_, tr,  newline,visited)



qn = int(input())
for _ in range(qn):
    start, end = map(int, input().split())
    visited = [0] * 10000
    length = float('inf')
    least = float('inf')
    path = None
    tr_in_path = set()
    dfs(start, end, [], 0,set(),None,visited)
    print(length - 1)
    pp = every_start = start
    for p in path[1:]:
        if p in tr_in_path or p == end:
            line = (which[pp] & which[p]).pop()
            print('Take Line#{} from {:0>4} to {:0>4}.'.format(line, every_start, p))
            every_start = p
        pp = p
