#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
for i in range(n):
    num = input()
    a = num[:len(num)//2]
    b = num[len(num)//2:]
    a,b = int(a), int(b)
    if a!= 0 and b != 0 and int(num)%(a*b) == 0:
        print('Yes')
    else:
        print('No')