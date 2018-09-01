#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import heapq as hq

N, M, K = map(int, input().split())
quota = list(map(int, input().split()))
l = [None] * N
app = [None] * N
for i in range(N):
    ge, gi, *q = map(int, input().split())
    gf = ge + gi # 算总成绩和平均成绩效果一样
    l[i] = [-gf, -ge, i]
    app[i] = q

h = sorted(l)
dstu = {}
dcount = {}

for stu in h:
    # stu: [gf, ge, id]
    id = stu[-1]
    grade = stu[:2]
    q = app[id]
    for school in q:
        num = dcount.setdefault(school, 0)
        idlist = dstu.setdefault(school, [])
        if num < quota[school] or grade == l[idlist[-1]][:2]:
            dcount[school] += 1
            dstu[school].append(id)
            break

for j in range(M):
    stulist = dstu.setdefault(j,[])
    stulist.sort()
    if len(stulist)==0:
        print('')
    else:
        print(*stulist)