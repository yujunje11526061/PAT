#!/usr/bin/env python
# -*- coding:utf-8 -*-
n,q = map(int, input().split())

nums = sorted(map(int, input().split()))

def find(x):
    s =0
    e = n-1
    while s<=e:
        mid = (s+e)//2
        if nums[mid]>=x:
            e = mid-1
        else:
            s= mid +1
    return s

for _ in range(q):
    x = int(input())
    if nums[-1] < x:
        print(0)
        continue
    location = find(x)
    print(n-location)
    for i in range(location,n):
        nums[i] -= 1
