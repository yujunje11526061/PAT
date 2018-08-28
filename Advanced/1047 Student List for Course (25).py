#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, K = map(int, input().split())

d = {}
for i in range(N):
    s = input().split()
    name, num, *course = s
    # course = map(int, course)
    for j in course:
        d.setdefault(j, []).append(name)

# print(d)
for i in range(1, K + 1):
    x = d.get(str(i), None)
    if x is None:
        print(i, 0)
        continue
    print(i, len(x))
    x.sort()
    print('\n'.join(x))
