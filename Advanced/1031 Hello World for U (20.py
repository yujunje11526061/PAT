#!/usr/bin/env.python
# -*- coding:utf-8 -*-
s = input()
n = len(s)
n += 2
def f(s, m):
    x = n-m-m-2
    for i in range(int(m-1)):
        print('{}{}{}'.format(s[i],' '*int(x), s[-1-i]))
    print(s[i+1:-1-i])

if n%3 == 0:
    m = n/3
    f(s,m)
elif (n-1)%3==0:
    m = (n-1)/3
    f(s,m)
else:
    m=(n-2)/3
    f(s,m)

