#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict
n,k,m = map(int,input().split())
sl = [None]+list(map(int, input().split()))

class stu():
    def __init__(self, id):
        self.id = id
        self.d = defaultdict(lambda :'-')

    def stat(self):
        self.tots = 0
        self.totc = 0
        self.flag = False
        for key, value in self.d.items():
            if value == -1 or value == '-':
                if value == -1:
                    self.d[key] = 0
                continue
            if value == sl[key]:
                self.totc += 1
            self.flag = True
            self.tots += value
        self.slr = [self.d[i] for i in range(1,k+1)]

    @property
    def record(self):
        return (-self.tots, -self.totc,self.id )

l = {}
for _ in range(m):
    id, p, s = map(int, input().split())
    x = l[id] if id in l else stu(id)
    if x.d[p] == '-' or x.d[p]<s:
        x.d[p] = s
    l[id] = x

def qualify(x):
    x.stat()
    return x.flag


l = filter(qualify, l.values())
l = sorted(l, key= lambda x:x.record)
ss = '{} {:0>5} {}' + ' {}'*k
r = 1
j = 2
sc = l[0].tots
print(ss.format(r, l[0].id, l[0].tots, *l[0].slr))
for p in l[1:]:
    if p.tots == sc:
        print(ss.format(r, p.id, p.tots, *p.slr))
    else:
        sc = p.tots
        r = j
        print(ss.format(r, p.id, p.tots, *p.slr))
    j += 1

