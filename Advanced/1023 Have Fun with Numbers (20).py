#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = input()
# s = set(iter(n))
d = {i:i for i in range(10)}
for i in n:
    d[int(i)] += 1

n2 = str(int(n)*2)
# s2 = set(iter(n))
d2 = {i:i for i in range(10)}
for i in n2:
    d2[int(i)] += 1

if len(n2) == len(n) and d == d2:
    print('Yes')
else:
    print('No')

print(n2)