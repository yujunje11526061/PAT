#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq

N, M, S, D = map(int, input().split())

table = [[] for i in range(N)]

for _ in range(M):
    i, j, w, f = map(int, input().split())
    table[i].append([w, f, j])
    table[j].append([w, f, i])

def Dijkstra(start, end): # 双权值最短路径
    inf =float('inf')
    visited = [0]*N
    dist = [inf]*N
    dist[start] = 0
    fee = [inf]*N
    fee[start] = 0
    heap = [(dist[start], start)]
    path = [None]*N
    while len(heap)>0:
        _, i = heapq.heappop(heap)
        if i == end:
            break
        if visited[i]:
            continue
        visited[i] = 1
        for w, f, j in table[i]:
            if not visited[j] and dist[i] + w <= dist[j]:
                if dist[i] + w < dist[j]:
                    dist[j] = dist[i] + w
                    fee[j] = fee[i] + f
                    path[j] = i
                    heapq.heappush(heap, (dist[j], j))
                elif fee[i] + f <= fee[j]:
                    fee[j] = fee[i] + f
                    path[j] = i

    return dist, path, fee

dist, path, fee = Dijkstra(S, D)
p = D
road = []
while p is not None:
    road.append(p)
    p = path[p]

print(*road[::-1], dist[D], fee[D])
