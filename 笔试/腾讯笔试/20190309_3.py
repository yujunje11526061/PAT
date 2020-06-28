#!/usr/bin/env python
# -*- coding:utf-8 -*-
n,s = map(int, input().split())

def reduce(start, end):
    tot = 1
    while start>end:
        tot *= start
        start -= 1
    return tot


if n<s:
    l = input()
    print(0)
elif n==s:
    l = input()
    print(1)
else:
    print(int(reduce(n,n-s)/reduce(s,1)*(2**(n-s))%(10**9+7)))