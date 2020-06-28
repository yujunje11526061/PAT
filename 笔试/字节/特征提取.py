#!/usr/bin/env python
# -*- coding:utf-8 -*-

N = int(input())


def calculate():
    maxS = 1
    M = int(input())
    consecutive = {}
    temp = {}
    for i in range(M):
        l = map(int, input().split())
        pairNum = next(l)
        for _ in range(pairNum):
            pair = (next(l), next(l))
            if pair in consecutive:
                cnt = consecutive[pair] + 1
                temp[pair] = cnt
                maxS = cnt if cnt>maxS else maxS
            else:
                temp[pair] = 1
        consecutive.clear()
        swap = consecutive
        consecutive = temp
        temp = swap

    return maxS


for i in range(N):
    print(calculate())