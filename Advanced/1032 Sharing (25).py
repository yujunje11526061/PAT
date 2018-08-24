#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
两个单链表入口
以一个入口遍历建立hash表
从另一个入口遍历另一个链表，如果在hash表中存在某个地址，说明找到了公共点，从此开始后面的肯定都是一样的（单链表），直接break
'''
s1, s2, N = input().split()
s1, s2 = int(s1), int(s2)
N = int(N)
dnext = {}
d1 = {}

for i in range(N):
    loc, name, nloc = input().split()
    loc, nloc = int(loc), int(nloc)
    dnext[loc] = nloc

p = s2

while p != -1:
    d1[p] = dnext[p]
    p = dnext[p]

q = s1
while q != -1:
    if d1.get(q) is not None:
        break
    q = dnext[q]

if q == -1:
    print(-1)
else:
    print('{:0>5}'.format(q))
