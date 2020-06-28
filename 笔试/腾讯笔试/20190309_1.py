#!/usr/bin/env python
# -*- coding:utf-8 -*-
n,m  = map(int, input().split())

cnt = 0
while (m>n):
    m = m-n
    cnt += 1

print(cnt+1)