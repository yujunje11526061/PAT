#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict

N = int(input())
l = map(int, input().split())
d = defaultdict(lambda: 0)


class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

maxdepth = 0
t = None
for i in l:
    p, pp = t, None
    count = 0
    while p is not None:
        if i <= p.value:
            pp = p
            p = p.left
        else:
            pp = p
            p = p.right
        count += 1
    if pp is None:
        t = node(i)
    else:
        if i <= pp.value:
            pp.left = node(i)
        else:
            pp.right = node(i)
    d[count] += 1
    if count> maxdepth:
        maxdepth = count

a = d[maxdepth]
b = d[maxdepth-1]
print('{} + {} = {}'.format(a,b,a+b))