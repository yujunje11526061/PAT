#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-
N,  M = map(int, input().split())
table = [[101 for j in range(N+1)] for i in range(N+1)]

for _ in range(M):
    i,j,d = map(int ,input().split())
    table[i][j] = d
    table[j][i] = d

K = int(input())

mindist = 999999
indexOfmindist = None
for k in range(1,K+1):
    seq = map(int,input().split())
    num = next(seq)
    if num <=  1:
        print("Path %d: NA (Not a TS cycle)" % k)
        continue
    count = N
    visited = [0]*(N+1)
    dist = 0
    pre = next(seq)
    start = pre
    count -= 1
    flag = 0
    visited[start] = 1
    for p in seq:
        if table[pre][p] <101:
            dist += table[pre][p]
            if not visited[p]:
                visited[p] = 1
                count -= 1
            pre = p
        else:
            flag = 1
            break
    if flag:
        print("Path %d: NA (Not a TS cycle)" % k)
        continue
    if pre == start and count == 0:
        if num-1==N :
            print(f"Path {k}: {dist} (TS simple cycle)")
        else:
            print(f"Path {k}: {dist} (TS cycle)")
        if dist<mindist:
            mindist = dist
            indexOfmindist = k
    else:
        print(f"Path {k}: {dist} (Not a TS cycle)")

print("Shortest Dist(%d) = %d" % (indexOfmindist,mindist))
