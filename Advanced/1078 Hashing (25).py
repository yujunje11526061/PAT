#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from math import  sqrt

size,n = map(int, input().split())

def isprime(x):
    if x == 1:
        return False
    for i in range(2,int(sqrt(x)+1)):
        if x%i==0:
            return False
    return True

while not isprime(size):
    size += 1

l = map(int, input().split())
table = [None]*size
where = []
for i in l:
    start = i%size
    p=start
    step = 0
    while table[p] is not None and step<size:
        step += 1
        p = (start+step*step)%size

    if step<size:
        table[p] = i
        where.append(p)
    else:
        where.append('-')

print(*where)