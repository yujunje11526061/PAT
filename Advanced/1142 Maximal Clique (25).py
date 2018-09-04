#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict

nv, ne = map(int, input().split())
d = defaultdict(set)
for _ in range(ne):
    i, j = map(int, input().split())
    d[i].add(j)
    d[j].add(i)
for v in range(1, nv + 1):
    d[v].add(v)
k = int(input())


def judge(num, seq):
    r = d[seq[0]]
    for id in range(1,num):
        r = r & d[seq[id]]
        if len(r) == 0:
            return 'Not a Clique'
    x = set(seq)
    if len(x-r)>0:
        return 'Not a Clique'
    elif len(r-x)>0:
        return 'Not Maximal'
    else:
        return 'Yes'


for _ in range(k):
    num, *seq = map(int, input().split())
    print(judge(num, seq))
