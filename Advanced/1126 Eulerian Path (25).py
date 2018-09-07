#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import deque
n,m = map(int, input().split())
degree = [0]*(n+1)
table2 = [[] for i in range(n+1)]
for _ in range(m):
    i,j = map(int ,input().split())
    degree[i] +=1
    degree[j] += 1
    table2[i].append(j)
    table2[j].append(i)

visited = [0]*(n+1)
count = 0
flag = 1
q = deque([1])
visited[1] = 1
num = 0
while len(q)>0:
    i = q.popleft()
    num +=1
    if degree[i] % 2 > 0:
        count += 1
    for j in table2[i]:
        if visited[j]:
            continue
        visited[j] = 1
        q.append(j)

if num<n:
    flag = 0


print(*degree[1:])
if flag==1 and count==0:
    print('Eulerian')
elif flag==1 and count ==2:
    print('Semi-Eulerian')
else:
    print('Non-Eulerian')