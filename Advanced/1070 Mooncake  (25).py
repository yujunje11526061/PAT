#!/usr/bin/env.python
# -*- coding:utf-8 -*-

N, D, = map(int, input().split())

storage = list(map(float, input().split()))
amount = list(map(float, input().split()))

unit = [(amount[i]/storage[i], i) for i in range(N)]

unit.sort(reverse=True)

profit = 0
for elem in unit:
    if storage[elem[1]] >= D:
        profit += D/storage[elem[1]]*amount[elem[1]]
        break
    else:
        profit += amount[elem[1]]
        D -= storage[elem[1]]

print('{:.2f}'.format(profit))
