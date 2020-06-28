#!/usr/bin/env python
# -*- coding:utf-8 -*-
N, D = map(int, input().split())

street = sorted(set(map(int, input().split())))

def find(x, i):
    s = i
    e = len(street) - 1
    while 0 <= s <= e < len(street):
        mid = (s + e) // 2
        if street[mid] < x:
            s = mid + 1
        elif street[mid] > x:
            e = mid - 1
        else:
            return mid
    return e

cnt = 0
for i in range(len(street)):
    j = find(street[i] + D, i)
    n = j - i - 1 if j>i else 0
    cnt += (n*(n+1)//2) % 99997867

print(cnt%99997867)
