#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
seq = sorted(map(int, input().split()))

if n%2 == 0:
    print(0, sum(seq[n//2:])-sum(seq[:n//2]))
else:
    print(1, sum(seq[(n-1)//2:])-sum(seq[:(n-1)//2]))