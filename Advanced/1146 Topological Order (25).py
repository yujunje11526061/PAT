#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
拓扑排序，建立一个出边，并维护一个入度表。
'''
N, M = map(int, input().split())
indegree = [0]*(N+1)
outdegree = [[] for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    outdegree[i].append(j)
    indegree[j] += 1

Check = int(input())

tpseq = []
for i in range(Check):
    ll = list(indegree)
    seq = map(int, input().split())
    for e in seq:
        if ll[e] != 0:
            tpseq.append(i)
            break
        for j in outdegree[e]:
            ll[j] -= 1

print(*tpseq)