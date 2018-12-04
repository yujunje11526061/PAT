#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input())
l = input()
bad = set()
hasprinted = set()

count = 1
pre = l[0]
for i in l[1:]:
    if i == pre:
        count += 1
    else:
        if count % n == 0:
            bad.add(pre)
        else:
            bad.discard(pre)
        count = 1
        pre = i

if count % n == 0:
    bad.add(pre)
else:
    bad.discard(pre)

i = 0
fs = "\n"
while i < len(l):
    fs += l[i]
    if l[i] in bad:
        if l[i:i+n] != l[i]*n:
            bad.discard(l[i])
            i += 1
        else:
            if(l[i] not in hasprinted):
                print(l[i], end="")
                hasprinted.add(l[i])
            i += n
    else:
        i += 1

print(fs)