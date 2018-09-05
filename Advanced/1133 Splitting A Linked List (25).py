#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
直接利用列表分类存储各个结点的地址就好
最后几个列表拼接，按总列表记录的顺序依次输出。
没必要去建类然后指来指去，1097也可以直接在数组上操作
'''
start, n, k = map(int, input().split())
l = [None] * 100000
for _ in range(n):
    id, value, ne = map(int, input().split())
    l[id] = [id, value, ne]

p = start
pp = None
l1 = []
l2 = []
l3 = []
while p != -1:
    if l[p][1]<0 or l[p][1]>k:
        if l[p][1]<0:
            l1.append(p)
        else:
            l2.append(p)
        p = l[p][2]
    else:
        l3.append(p)
        pp = l[p][0]
        p = l[p][2]

ll = l1+l3+l2
for i in range(len(ll)-1):
    print('{:0>5} {} {:0>5}'.format(*l[ll[i]][:2], l[ll[i+1]][0]))

print('{:0>5} {} {}'.format(*l[ll[-1]][:2], -1))



