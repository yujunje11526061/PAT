#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())

def ispn(x):
    x = str(x)
    i,j = 0, len(x)-1
    while i<j:
        if x[i]!=x[j]:
            return False
        i += 1
        j -= 1
    return True

flag = 1
for i in range(10): # 迭代10次，判断11次
    if ispn(n):
        print('{} is a palindromic number.'.format(n))
        flag = 0
        break
    else:
        m = int(str(n)[::-1])
        nm = n+m
        print('{} + {} = {}'.format(n,m,nm))
        n = nm

if flag:
    print('Not found in 10 iterations.')