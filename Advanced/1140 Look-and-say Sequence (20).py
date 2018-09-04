#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import OrderedDict

D,N = input().split()
N = int(N)
if N == 1:
    print(D)
else:
    for i in range(N-1):
        d = []
        s= ''
        for j in D:
            try:
                if d[-1][0] == j:
                    d[-1][1] += 1
                else:
                    d.append([j,1])
            except IndexError:
                d.append([j,1])
        for key, value in d:
            s += str(key)+str(value)
        D= s

    print(s)