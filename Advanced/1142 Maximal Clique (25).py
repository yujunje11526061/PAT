#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict

nv, ne = map(int, input().split())
d = defaultdict(set)
for _ in range(ne):
    i, j = map(int, input().split())
    d[i].add(j)
    d[j].add(i)
for v in range(1, nv + 1):  # 自己也要包括
    d[v].add(v)
k = int(input())


def judge(num, seq):
    r = d[seq[0]]
    for id in range(1,num):
        r = r & d[seq[id]]
        if len(r) == 0:
            return 'Not a Clique'
    x = set(seq)
    if len(x-r)>0: # 所求序列与最终交集的差集，不为空说明有的没进去
        return 'Not a Clique'
    elif len(r-x)>0: # 在上一条件基础上，最终交集与所求序列的差集，不为空说明有更多可以加
        return 'Not Maximal'
    else: # 恰好，则就是最大Clique
        return 'Yes'


for _ in range(k):
    num, *seq = map(int, input().split())
    print(judge(num, seq))
