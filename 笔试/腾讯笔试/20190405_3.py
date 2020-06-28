#!/usr/bin/env python
# -*- coding:utf-8 -*-
N = int(input())

attack = list(map(int, input().split()))
need = list(map(int, input().split()))
tot = 0
import heapq
hq = []
totatt = 0
for i,att in enumerate(attack):
    if totatt<att:
        if len(hq)==0:
            totatt += att
            tot += need[i]
        else:
            maxPrev, index = hq[0]
            maxPrev = -maxPrev
            if need[i] <= need[index]:
                totatt += att
                tot += need[i]
            else:
                if maxPrev+totatt<att:
                    totatt += att
                    tot += need[i]
                else:
                    totatt += maxPrev
                    tot += need[index]
                    heapq.heappop(hq)
                    heapq.heappush(hq, (-att, i))
    else:
        heapq.heappush(hq, (-att,i))

print(tot)
