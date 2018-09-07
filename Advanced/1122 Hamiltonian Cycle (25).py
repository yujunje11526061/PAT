#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n, m = map(int, input().split())
table = [set() for i in range(n+1)]
for i in range(m):
    i, j = map(int, input().split())
    table[i].add(j)
    table[j].add(i)

def judge():
    if num<n or seq[0] != seq[-1]:
        return 'NO'
    visited = [0]*(n+1)
    for i in range(num-1):
        if seq[i+1] not in table[seq[i]]:
            return 'NO'
        if visited[seq[i]]:
            return 'NO'
        visited[seq[i]] = 1

    return 'YES' if sum(visited) == n else 'NO'



k = int(input())
for _ in range(k):
    num,*seq = map(int, input().split())
    print(judge())
