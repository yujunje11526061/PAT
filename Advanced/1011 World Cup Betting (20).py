#!/usr/bin/env.python
# -*- coding:utf-8 -*-

a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = list(map(float, input().split()))

d = {0:'W',1:'T',2:'L'}

a1 = max(a)
a2 = d[a.index(a1)]

b1 = max(b)
b2 = d[b.index(b1)]

c1 = max(c)
c2 = d[c.index(c1)]

pro = (a1*b1*c1*0.65-1)*2+0.001

print('{} {} {} {:.2f}'.format(a2,b2,c2,pro))
