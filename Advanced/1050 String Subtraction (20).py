#!/usr/bin/env.python
# -*- coding:utf-8 -*-
s1 = input()
s2 = input()
s = set(s2)
for i in s1:
    if not i in s:
        print(i,end= '')