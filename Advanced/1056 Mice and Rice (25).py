#!/usr/bin/env.python
# -*- coding:utf-8 -*-
import math
np, ng = map(int, input().split())
w = list(map(int, input().split()))
seq = list(map(int, input().split()))

rank = [None]*np
while len(seq) > 1:
    tot = len(seq)
    g = math.ceil(tot/ng)
    newseq = []
    for i in range(g):
        l = []
        members = seq[i*ng:(i+1)*ng]
        if len(members) == 1:
            newseq.append(members[0])
            break
        for id in members:
            l.append((w[id], id))
        l.sort(reverse=True)
        for p in l[1:]:
            rank[p[1]] = g+1
        newseq.append(l[0][1])
    seq = newseq

rank[seq[0]]=1
print(*rank)