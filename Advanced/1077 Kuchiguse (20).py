#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input())

l = []
for i in range(n):
    l.append(input()[::-1])

minlength = len(min(l, key=len))

flag =1
for i in range(minlength):
    j = 0
    x = l[0][i]
    for s in l:
        if s[i] != x:
            flag = 0
            break
        j += 1
    if flag==0:
        break

if flag==1:
    print(l[0][i::-1])
elif i >0:
    print(l[0][i-1::-1])
else:
    print("nai")