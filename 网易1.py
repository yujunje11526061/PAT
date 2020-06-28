#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input())

score = list(map(int, input().split()))

sortedScore = sorted(score)

def binaryFind(x):
    s,e = 0,n-1
    while s<=e:
        mid = (s+e)//2
        if sortedScore[mid]<=x:
            s = mid+1
        else:
            e = mid-1
    return e

q = int(input())
for _ in range(q):
    id = int(input())-1
    sc = score[id]
    num = binaryFind(sc)
    p = (num)/n*100
    print("{:.6f}".format(p))
