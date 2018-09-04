#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict
N = int(input())
count = defaultdict(lambda :0)
tot = defaultdict(lambda :0)
d = {'B':2/3, 'A':1,'T':1.5}

for i in range(N):
    id, score, sch = input().split()
    score = int(score)
    sch = sch.lower()
    count[sch] += 1
    tot[sch] += score* d[id[0]]

num = len(tot)
print(num)
keys = tot.keys()
xx = [(-int(tot[k]), count[k], k) for k in keys]
xx.sort()
p,rank = 1,1
q = xx[0][0]
for sc, ns, name in xx:
    if sc == q:
        print(p, name, -sc, ns)
    else:
        print(rank, name, -sc, ns)
        p = rank
        q = sc
    rank += 1