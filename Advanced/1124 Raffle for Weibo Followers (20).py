#!/usr/bin/env.python
# -*- coding:utf-8 -*-
m,n,s = map(int, input().split())
j = s
ss = set()
i = 1
if s>m:
    print('Keep going...')

else:
    while i<=m:
        name = input()
        if i-s>0 and (i-s)%n==0:
            i += 1
            while name in ss and i<=m:
                name = input()
                s += 1 # 从获奖的人后面开始跳，if语句中判断用的起始点要修正
                i += 1
            ss.add(name)
            print(name)
        else:
            i+=1