#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
 元素序列里找第一个不重复的元素。OrderedDict的使用，继承自Dict
'''
from collections import OrderedDict, MutableSet

l = map(int, input().split())

n = next(l)
od = OrderedDict()
d = {}
while 1:
    try:
        x = next(l)
        if x in od:
            od.__delitem__(x)
            d[x] = 1
        elif x not in d:
            od[x] = 1
    except StopIteration:
        break

if len(od) == 0:
    print('None')
else:
    for key, value in od.items():
        print(key)
        break
