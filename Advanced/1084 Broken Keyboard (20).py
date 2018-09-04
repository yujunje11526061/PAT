#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import OrderedDict
s1 = input()
s2 = input()
sset = set(iter(s2))
lostdict = {}
for i in s1:
    if i not in sset:
        lostdict[i.capitalize()] = 1

for key in lostdict.keys():
    print(key,end='')

