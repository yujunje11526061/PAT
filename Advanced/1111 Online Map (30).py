#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq as hq
N,M= map(int, input().split())
table = [[] for i in range(N)]
inf = float('inf')
ll  = [[inf]*N for i in range(N)]
tt  = [[inf]*N for i in range(N)]
cc  = [[inf]*N for i in range(N)]
for _ in range(M):
    i,j,f,l,t = map(int, input().split())
    table[i].append(j)
    ll[i][j] = l
    tt[i][j] = t
    cc[i][j] = 1
    if not f:
        table[j].append(i)
        ll[j][i] = l
        tt[j][i] = t
        cc[j][i] = 1

s , e= map(int, input().split())
road = []
record = []
for sta in range(2):
    w1,w2 = (tt,cc) if sta else (ll,tt)
    visited = [0]*N
    path = [None]*N
    dist = [inf]*N
    dist[s] = 0
    dist2 = [inf] * N
    dist2[s] = 0
    h = [[dist[s], s]]
    while len(h)>0:
        _,i = hq.heappop(h)
        if i == e:
            break
        if visited[i]:
            continue
        visited[i] = 1
        for j in table[i]:
            if visited[j]:
                continue
            if dist[j] > dist[i] + w1[i][j]:
                dist[j] = dist[i]+w1[i][j]
                dist2[j] = dist2[i] + w2[i][j]
                path[j] = i
                hq.heappush(h, [dist[j],j])
            elif dist[j] == dist[i] +w1[i][j]:
                if dist2[j] > dist2[i] + w2[i][j]:
                    dist2[j] = dist2[i] +w2[i][j]
                    path[j] = i
    p = e
    r = []
    record.append(dist[e])
    while p != s:
        r.append(p)
        p = path[p]
    # r.reverse()
    road.append(r)

if road[0] == road[1]:
    s2 = ' -> {}'*len(road[0])
    s1 = 'Distance = {}; Time = {}: {}'+s2
    print(s1.format(record[0],record[1], s, *road[0][::-1]))
else:
    s2 = ' -> {}' * len(road[0])
    s4 = ' -> {}' * len(road[1])
    s1 = 'Distance = {}: {}'+s2
    s3 = 'Time = {}: {}'+s4
    print(s1.format(record[0],s, *road[0][::-1]))
    print(s3.format(record[1],s, *road[1][::-1]))