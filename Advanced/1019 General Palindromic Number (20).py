#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n, b = map(int, input().split())
n2 = n
m = []
while n>0:
    n, k = divmod(n, b)
    m.append(k)

i, j = 0, len(m)-1
while i<j:
    if m[i]==m[j]:
        i += 1
        j -= 1
    else:
        break

if i>=j:
    print('Yes')
else:
    print('No')
if n2 > 0:
    m.reverse()
    print(*m)
else:
    print(0)