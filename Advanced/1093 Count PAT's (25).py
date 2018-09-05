#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
从头扫描看每个A前面几个P，从后扫描，看每个A后面几个T
'''
from collections import defaultdict
s = input().lstrip('AT').rstrip('AP')

d= defaultdict(lambda : 0)

cp = 0
for i in range(len(s)):
    if s[i] == 'A':
        d[i] = cp
    elif s[i] == 'P':
        cp += 1

ct = 0
tot = 0
for j in range(len(s)-1,-1,-1):
    if s[j] == 'A':
        tot += d[j]*ct
    elif s[j] == 'T':
        ct += 1

print(tot%1000000007)
