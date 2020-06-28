#!/usr/bin/env python
# -*- coding:utf-8 -*-


n,m = map(int,input().split())
if(n<m):
    l = input()
    print(-1)
else:
    l = input().split()
    d = {}
    i,j = 0,0
    cnt = 0
    minCnt = 9999999999
    while j<len(l):
        if 0<int(l[j])<=m:
            if l[j] in d:
                d[l[j]] += 1
                while i<j and d[l[i]]>1:
                    d[l[i]] -= 1
                    i += 1

            else:
                d[l[j]] = 1
            if len(d)==m and j-i+1<minCnt:
                minCnt =j-i+1
        j += 1

    if minCnt<9999999999:
        print(minCnt)
    else:
        print(-1)