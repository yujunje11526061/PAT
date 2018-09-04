#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
用好集合
'''
from collections import defaultdict

N, M = map(int, input().split())
table = defaultdict(set)


def gender(person):
    return 0 if person[0] == '-' else 1


for i in range(M):
    a, b = input().split()
    table[a].add(b)
    table[b].add(a)


K = int(input())
for _ in range(K):
    a, b = input().split()
    fa = {i for i in table[a] if gender(i)==gender(a)}
    fa.discard(b)
    fb = {j for j in table[b] if gender(j)==gender(b)}
    fb.discard(a)
    line = []
    for i in fa:
        for j in fb:
            if i in table[j]:
                line.append([abs(int(i)),abs(int(j))])
    print(len(line))
    line.sort()
    for x,y in line:
        print('{:0>4} {:0>4}'.format(x,y))

