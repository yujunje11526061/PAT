#!/usr/bin/env.python
# -*- coding:utf-8 -*-
# from collections import defaultdict
n = int(input())
seq = input().split()

# d = defaultdict(lambda :0)
ss = set()

for num in seq:
    l = sum(map(int, list(num)))
    # d[l] += 1
    # if d[l] >=2:
    ss.add(l)

print(len(ss))
print(*sorted(ss))