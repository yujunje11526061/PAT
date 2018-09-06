#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
dd = "tret, jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec".split(', ')
dd2 = "tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou".split(', ')
def to_mar(s):
    x = int(s)
    sx = []
    if x== 0:
        sx = ["tret"]
    elif x<13:
        sx=[dd[x]]
    else:
        a,b = divmod(x,13)
        sx.append(dd2[a-1])
        if b != 0:
            sx.append(dd[b])
    return sx

def to_earth(s):
    x = s.split()
    if len(x)>1:
        a, b = x
        sx = 13*(dd2.index(a)+1)+ dd.index(b)
    else:
        try:
            sx = dd.index(x[0])
        except:
            sx = (dd2.index(x[0])+1)*13
    return sx


for i in range(n):
    s = input()
    if '0'<=s[0]<='9':
        print(*to_mar(s))
    else:
        print(to_earth(s))