#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq as hq

N, K, start = input().split()
N, K = int(N), int(K)
dname = {start: 0}
did = [None] * N
did[0] = start
dhappy = [0] * N
for i in range(1, N):
    name, happy = input().split()
    happy = int(happy)
    dname[name] = i
    did[i] = name
    dhappy[i] = happy

end = dname['ROM']

table = [[] for i in range(N)]
for _ in range(K):
    i, j, w = input().split()
    i, j, w = dname[i], dname[j], int(w)
    table[i].append([j, w])
    table[j].append([i, w])

path = [[] for i in range(N)]
inf = float('inf')

def Dijkstra(s, e):
    visited = [0] * N

    dist = [inf] * N
    dist[s] = 0
    h = [0] * N
    l = [[0, s]]
    count = [0] * N
    count[0] = 1
    while len(l) > 0:
        _, i = hq.heappop(l)
        if visited[i]:
            continue
        if i == e:
            return count[i], dist[i]
        visited[i] = 1
        for j, w in table[i]:
            if visited[j]:
                continue
            if dist[j] > dist[i] + w: # 第一权更新后，务必检查是否所有指标都更新了，是否入队了
                dist[j] = dist[i] + w
                path[j] = [i]
                count[j] = count[i]
                h[j] = h[i]+dhappy[j]
                hq.heappush(l, [dist[j], j])
            elif dist[j] == dist[i] + w: # 碰到分支记得检查哪些要更新，哪些不用
                count[j] += count[i]
                if h[j] < h[i] + dhappy[j]:
                    h[j] = h[i] + dhappy[j]
                    path[j] = [i]
                elif h[j] == h[i] + dhappy[j]:
                    path[j].append(i)


count,cost = Dijkstra(0, end)
all_roads = []
# 不断传列表记录路径，能走出来的就是最终路径，当然这里是回溯，必然能走出。此写法类似背包问题递归写法输出所有组合
def dfs(e, s, xl):
    ll = list(xl)
    if e == s:
        ll.append(e)
        all_roads.append(ll)
        return
    p = e
    ll.append(e)
    pre = path[p]
    for i in pre:
        dfs(i, s, ll)

dfs(end, 0, [])
final = None
length = inf
for r in all_roads:
    if len(r) < length:
        length = len(r)
        final = r

tot = 0
for i in final:
    tot += dhappy[i]

avg = tot//(length-1)
print(count, cost, tot, avg)
print(did[i], end='')
for i in final[-2::-1]:
    print('->{}'.format(did[i]), end='')
