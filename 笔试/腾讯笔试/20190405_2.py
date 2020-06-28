#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input())
ss = input()
l = [0,0]
for s in ss:
    l[int(s)] +=1

print(abs(l[0]-l[1]))