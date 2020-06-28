#!/usr/bin/env python
# -*- coding:utf-8 -*-

n, L = map(int, input().split())
l = list(map(int, input().split()))

def reduce(x):
    tot = 1
    while x>1:
        tot *= x
        x -= 1
    return tot

maxcnt = 1
for i in range(1,n):
    if l[i] != l[i-1]:
        maxcnt +=1
# print(maxcnt)
if maxcnt<L:
    print(0)
elif maxcnt==L and n==L:
    print(1)
else:
    pass