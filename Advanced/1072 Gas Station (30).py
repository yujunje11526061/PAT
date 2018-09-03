#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq as hq

N, M, K, D = map(int, input().split())
idg = {'G{}'.format(i): N + i for i in range(1, M + 1)}
n = M + N + 1
inf = float('inf')
table = [[] * n for i in range(n)]
w = [[inf] * n for i in range(n)]
for i in range(K):
    i, j, distance = input().split()
    if i[0] == 'G':
        i = idg[i]
    if j[0] == 'G':
        j = idg[j]
    i,j, distance =int(i), int(j), int(distance)
    if distance < w[i][j]:
        w[i][j] = distance
        w[j][i] = distance
    table[i].append(j)
    table[j].append(i)

maxmindist = 0
minlist = []
avg = inf
for start in range(N + 1, N + M + 1):
    visited = [0] * n
    dist = [inf] * n
    dist[start] = 0
    h = [[dist[start], start]]
    count = 0
    while len(h) > 0:
        distxx, i = hq.heappop(h)
        if distxx > D:
            break
        if visited[i]:
            continue
        visited[i] = 1
        count += 1
        if count == M + N:
            break
        for j in table[i]:
            if visited[j]:
                continue
            if dist[j] > dist[i] + w[i][j]:
                dist[j] = dist[i] + w[i][j]
                hq.heappush(h, [dist[j], j])

    if count == N + M:
        x = min(dist[1:N + 1])
        if x > maxmindist:
            maxmindist = x
            minlist = [start]
            avg = sum(dist[1:N + 1])/N
        elif x == maxmindist:
            avg_ = sum(dist[1:N + 1])/N
            if avg_ < avg:
                avg = avg_
                minlist = [start]
            elif avg_ == avg:
                minlist.append(start)
if len(minlist)==0:
    print('No Solution')
else:
    best = min(minlist)
    print('G{}'.format(best-N))
    print('{:.1f} {:.1f}'.format(maxmindist, avg))
