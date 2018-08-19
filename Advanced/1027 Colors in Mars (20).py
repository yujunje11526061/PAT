#!/usr/bin/env.python
# -*- coding:utf-8 -*-
a, b, c = map(int, input().split())

d = {10:'A',11:'B',12:'C'}
def cal(x):
    l = ''
    while x > 0:
        x,j = divmod(x,13)
        if j>9:
            j = d[j]
        l = l+str(j)
    return l[::-1]


a = cal(a)
b = cal(b)
c = cal(c)

print('#{:0>2}{:0>2}{:0>2}'.format(a,b,c))
