#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from math import gcd

n = int(input())
seq = input().split()
x, y = map(int, seq[0].split('/'))
for word in seq[1:]:
    a, b = map(int, word.split('/'))
    x, y = x * b + y * a, y*b
    g = gcd(abs(x), abs(y))
    x, y = x // g, y // g


if x == 0:
    print(0)
else:
    flag = 0
    if x*y<0:
        flag = 1
    x, y = abs(x), abs(y)
    if x>=y:
        i,j = divmod(x,y)
        if j==0:
            if flag:
                print('-{}'.format(i))
            else:
                print(i)
        else:
            if flag:
                print(i if j==0 else '{} -{}/{}'.format(i,j,y))
            else:
                print(i if j == 0 else '{} {}/{}'.format(i, j, y))
    else:
        if flag:
            print('-{}/{}'.format(x,y))
        else:
            print('{}/{}'.format(x, y))

