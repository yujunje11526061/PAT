#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
coupled = [None]*100000
for _ in range(n):
    i, j = map(int, input().split())
    coupled[i] = j
    coupled[j]= i

m = int(input())
q = map(int, input().split())
party = set()
for i in q:
    if coupled[i] is None:
        party.add(i)
    elif coupled[i] in party:
        party.remove(coupled[i])
    else:
        party.add(i)

l = sorted(party)
s = ['{:0>5}']*len(l)
s = ' '.join(s)
print(len(l))
if len(l)>0:
    print(s.format(*l))