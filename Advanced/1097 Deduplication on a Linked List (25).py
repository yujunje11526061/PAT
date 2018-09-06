#!/usr/bin/env.python
# -*- coding:utf-8 -*-

s, n = map(int, input().split())
l = [None] * 100000
for _ in range(n):
    id, key, nextid = map(int, input().split())
    l[id] = [id, key, nextid]


l0 = []
lx = []
if l[s] is None:
    # print(None)
    pass
else:
    p = s
    pp = None
    record = set()
    while p != -1:
        this = l[p]
        if abs(this[1]) not in record:
            record.add(abs(this[1]))
            l0.append(p)
        else:
            lx.append(p)
        p = this[2]

if len(l0)==0:
    pass
else:
    for i in range(len(l0)-1):
        print('{:0>5} {} {:0>5}'.format(*l[l0[i]][:2], l[l0[i+1]][0]))

    print('{:0>5} {} {}'.format(*l[l0[-1]][:2], -1))

if len(lx) == 0:
    pass
else:
    for i in range(len(lx) - 1):
        print('{:0>5} {} {:0>5}'.format(*l[lx[i]][:2], l[lx[i + 1]][0]))

    print('{:0>5} {} {}'.format(*l[lx[-1]][:2], -1))
