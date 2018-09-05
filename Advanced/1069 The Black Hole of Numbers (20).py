#!/usr/bin/env.python
# -*- coding:utf-8 -*-
s = int(input())
s = '{:0>4}'.format(s)

l = list(s)
if l[0] == l[1] ==l[2]==l[3]:
    print(s,'-',s,'=','0000')
elif s == '6174':
    print('7641 - 1467 = 6174')
else:
    while s != '6174':
        l.sort()
        x = int(''.join(l))
        y = int(''.join(l[::-1]))
        diff = y-x
        s = '{:0>4}'.format(diff)
        l = list(s)
        print('{:0>4} - {:0>4} = {:0>4}'.format(y,x,diff))
