#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, Q = map(int, input().split())

d = [[] for i in range(201)]
for i in range(N):
    name, age, welth = input().split()
    age = int(age)
    welth = -int(welth)
    d[age].append([welth, age, name])

# l.sort(key = lambda x:x[1:])

for i in range(1, Q + 1):
    print('Case #{}:'.format(i))
    num, start, end = map(int, input().split())
    l = sum(d[start:end + 1], [])
    if len(l) == 0:
        print('None')
    else:
        l.sort()
        for item in l[:num]:
            print(item[2], item[1], -item[0])
