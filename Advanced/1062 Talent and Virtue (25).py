#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n, l ,h = map(int, input().split())
class person():
    def __init__(self, id, vg,tg):
        self.id = id
        self.vg = vg
        self.tg = tg
        self.tot = -(tg+vg)
        self.record = (self.tot, -self.vg,id)
sage = []
nobelmen = []
fool = []
rest = []

for _ in range(n):
    id, vg,tg = map(int, input().split())
    if vg<l or tg<l:
        continue
    elif vg>=h and tg>=h:
        sage.append(person(id,vg,tg))
    elif vg>=h and tg<h:
        nobelmen.append(person(id,vg,tg))
    elif tg<=vg and tg<h and vg<h:
        fool.append(person(id,vg,tg))
    else:
        rest.append(person(id,vg,tg))

sage.sort(key = lambda x:x.record)
nobelmen.sort(key = lambda x:x.record)
fool.sort(key = lambda x:x.record)
rest.sort(key = lambda x:x.record)
print(len(sage)+len(nobelmen)+len(fool)+len(rest))
for cls in (sage,nobelmen,fool,rest):
    for p in cls:
        print('{:0>8} {} {}'.format(p.id, p.vg,p.tg))
