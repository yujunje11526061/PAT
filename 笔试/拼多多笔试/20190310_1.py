#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input())

a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), key = lambda x:-x)

S = 0

for i, j in zip(a,b):
    S += i*j
print(S)

