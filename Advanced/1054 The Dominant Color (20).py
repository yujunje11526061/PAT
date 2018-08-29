#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict

M, N = map(int, input().split())


def f():
    d = defaultdict(lambda: 0)
    for i in range(N):
        C = map(int, input().split())
        for c in C:
            d[c] += 1
            if d[c] > N * M / 2:  # 超过半数则直接返回，不用继续扫描了，一定最大
                return c

print(f())
