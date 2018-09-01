#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
带层数的广度优先搜索，题意，只有L层（包括L）内的人才会被统计
'''
from collections import deque
N,L = map(int, input().split())
table = [[] for i in range(N+1)]
for i in range(1,N+1):
    _, *l = map(int, input().split())
    for j in l:
        table[j].append(i)

_, *querys = map(int, input().split())

def bfs(s, L):
    q = deque()
    d = {}
    level = 0
    d[s] = level
    q.append(s)
    visited = [0]*(N+1)
    visited[s] = 1
    count = 0
    while len(q)>0:
        p = q.popleft()
        if d[p] == L:
            return count
        for i in table[p]:
            if visited[i]:
                continue
            visited[i] = 1
            d[i] = d[p]+1
            q.append(i)
            count += 1
    return count
if N == 1:
    print(0)
else:
    for query in querys:
        print(bfs(query,L))
