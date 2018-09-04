#!/usr/bin/env.python
# -*- coding:utf-8 -*-
a, b = input().split()
i,j,k = map(int, a.split('.'))
o,p,q = map(int, b.split('.'))
l,m,n = i+o, j+p, k+q
m, n = m+n//29, n%29
l,m = l+m//17, m%17

print('{}.{}.{}'.format(l,m,n))
