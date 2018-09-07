#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
l = sorted(map(int, input().split()))


def find_max(s, e, x):
    head, tail = s, e
    while s <= head <= tail <= e:
        mid = (head + tail) // 2
        if l[mid] <= x:
            head = mid + 1
        else:
            tail = mid - 1
    return tail



id = n - 1
for e in range(min(l[-1],n), -1, -1):
    id = find_max(0, id, e)  # 有num个比e大的
    num = n - 1 - id
    if e <= num:  # 比e大的个数刚好够着e的大小，e不能再小了
        break

print(e)
