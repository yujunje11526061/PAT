#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
题意时从里面选，来组成完美序列，不用按照原顺序
排序，下界扫描时二分找上界
'''
n, p = map(int, input().split())
seq  = sorted(map(int, input().split()))

def find_max(s,e,x):
    head,tail = s,e
    while s<=head<=tail<=e:
        mid = (head+tail)//2
        if seq[mid]<=x:
            head = mid+1
        else:
            tail = mid-1
    return tail

maxl = 0
end = 0
for i in range(n):
    start = i
    x = seq[start]*p
    end = find_max(end,n-1,x)
    end = n-1 if end>=n else end
    count = end-start+1
    if count>maxl:
        maxl=count

print(maxl)

