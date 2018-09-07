#!/usr/bin/env.python
# -*- coding:utf-8 -*-
d = {'-':'Fu', '1':'yi',  '2':'er',  '3':'san', '4':'si', '5':'wu',\
     '6':'liu','7':'qi', '8':'ba', '9':'jiu'}

s = list(input())
s2 = []
if s[0] == '-':
    s2.append(d['-'])
s = s[1:]
for i in s:
    s2.append(d[i])
