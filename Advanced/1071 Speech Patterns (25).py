#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict
s = input().split()
d = defaultdict(lambda :0)
maxt = 0
maxword = None
for word in s:
    word = word.strip('`~!@#$%^&*()-_=+\\|]}\'\"[{;:/?.,><').lower()
    d[word] += 1
    if d[word] > maxt or (d[word]==maxt and word<maxword):
        maxt = d[word]
        maxword = word
print(maxword, maxt)
