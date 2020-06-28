#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input())

l = list(map(int, input().split()))

MIN = min(l)
MAX = max(l)

def test(E):
    for height in l:
        if height>E:
            E -= height-E
        else:
            E += E- height
        if E<0:
            return False
    return True


for E in range(MIN,MAX+1):
    if test(E):
        print(E)
        break
