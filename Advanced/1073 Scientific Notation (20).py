#!/usr/bin/env.python
# -*- coding:utf-8 -*-
s = input().split("E")
num, exp = s[0], s[1]
exp2 = int(exp[1:])
sign = num[0]
inte, frac = num[1:].split('.')
if exp[0] == '-':
    ss = '0.' + '0' * (exp2 - 1) + inte + frac
else:
    length = len(frac)
    left = exp2 - length
    if left >= 0:
        ss = inte + frac + '0' * left
    else:
        f1, f2 = frac[:exp2], frac[exp2:]
        ss = inte + f1 + '.' + f2

if sign == '-':
    ss = sign + ss
print(ss)
