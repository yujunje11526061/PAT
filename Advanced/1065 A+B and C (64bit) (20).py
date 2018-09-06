#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
for i in range(n):
    t = 'false'
    a,b,c = map(int, input().split())
    if a+b>c:
        t = 'true'
    print('Case #{}: {}'.format(i+1, t))