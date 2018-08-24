#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
从两个队列头里获取并剔除小的那一个的思想
'''

l1 = map(int, input().split())
l2 = map(int, input().split())

n1 = next(l1)
n2 = next(l2)
flag = (n1 + n2 - 1)//2 # 表示总共要剔除几个，然后在两个队列头中取小的那个。如果直接算出中位数是第几个，然后数剔除到第几个的话，循环条件容易写错
# print(flag)

a = next(l1)
b = next(l2)  # 用生成器获取，节约内存
c1 = 1
c2 = 1
c3 = 0 # 表示剔除了几个
while c3 < flag and c1<n1 and c2<n2:
    if a < b and c1<n1:
            a = next(l1) # 获取一个新定a， 旧的被剔除
            c1 += 1
            c3 += 1
    elif b<=a and c2<n2:
            b = next(l2)
            c2 += 1
            c3 += 1


if c3 == flag:
    print(min(a,b))
elif c1 == n1:
    while c3 < flag:
        cnt = next(l2)
        c3 += 1
    print(cnt)
else:
    while c3 < flag:
        cnt = next(l1)
        c3 += 1
    print(cnt)

