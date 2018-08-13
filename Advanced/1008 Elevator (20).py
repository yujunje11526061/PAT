#!/usr/bin/env.python
# -*- coding:utf-8 -*-
aaaa = list(map(int, input().split()))
n, l = aaaa[0], aaaa[1:]

j = 0
tot = 0
for i in l:
    dif = i-j
    if dif >0:
        tot += (6 * dif + 5)
    else:
        tot += (-4*dif + 5)
    j = i

print(tot)
