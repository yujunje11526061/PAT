#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict
s1 = input()
s = input()

need = defaultdict(lambda :0)
for i in s:
    need[i] += 1

count = 0
for j in s1:
    if need[j] > 0:
        need[j] -= 1
        count += 1

if count ==len(s):
    print('Yes', len(s1)-len(s))
else:
    print('No',len(s)-count)
