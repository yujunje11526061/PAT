#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
平方探测法解决冲突 H(key)i = (H(key)0 + i**2) % TSize
由
    (H(key)0 + (TSize + i)**2) % TSize
= (H(key)0 + i**2 + TSize**2 + 2*i*TSize) % TSize
= (H(key)0 + i**2) % TSize
可知
单向探测时，最大的探测次数为TSize+1
双向时，最大的探测次数为2*TSize
'''
from math import sqrt

MS, N, M = map(int, input().split())


def isprime(n):
    if n == 1:
        return False
    limit = int(sqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

if MS<=2:
    MS =2
elif MS % 2 == 0:
    MS += 1

while not isprime(MS):
    MS += 2

I = map(int, input().split())
table = [None] * MS
for i in I:
    dis = 0
    cnt = 0
    while dis <= MS:
        loc = (i + dis ** 2) % MS
        cnt += 1
        if table[loc] is None:
            table[loc] = i
            break
        else:
            dis += 1
    if dis > MS:
        print(i, 'cannot be inserted.')

total = 0

seq = map(int, input().split())
for i in seq:
    dis = 0
    cnt = 0
    while dis <= MS:
        loc = (i + dis ** 2) % MS
        cnt += 1
        if table[loc] is None:  # 不在表中
            break
        elif table[loc] == i: # 找到了
            break
        else:  # 没找到, 继续探测
            dis += 1
    total += cnt

print('{:.1f}'.format(total/M))

