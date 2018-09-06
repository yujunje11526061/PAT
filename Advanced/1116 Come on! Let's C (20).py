#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict
from math import sqrt
def isprime(x):
    up = int(sqrt(x))
    for i in range(2,up+1):
        if x%i == 0:
            return False
    return True

d = defaultdict(lambda :0)
n = int(input())
for i in range(1,n+1):
    id = int(input())
    d[id] = i

k = int(input())
for j in range(k):
    q = int(input())
    if d[q] ==-1:
        print('{:0>4}: Checked'.format(q))
    elif d[q]==0:
        print('{:0>4}: Are you kidding?'.format(q))
    elif d[q] == 1:
        print('{:0>4}: Mystery Award'.format(q))
        d[q] = -1
    elif isprime(d[q]):
        print('{:0>4}: Minion'.format(q))
        d[q] = -1
    else:
        print('{:0>4}: Chocolate'.format(q))
        d[q] =-1