#!/usr/bin/env.python
# -*- coding:utf-8 -*-
P, M, N = map(int, input().split())


class stu():
    def __init__(self, name, pro=-1, mid=-1, fin=-1):
        self.name = name
        self.pro = pro
        self.mid = mid
        self.fin = fin

    @property
    def _end(self):
        if self.fin >= self.mid:
            self.end = self.fin
        else:
            self.end = round(self.mid * 0.4 + self.fin * 0.6)  # 要在排序前先round
        return self.end

    def isq(self):
        if self.pro < 200 or self._end < 60:
            return False
        return True

    @property
    def record(self):
        return [-self.end, self.name]


d = {}
for i in range(P):
    name, pro = input().split()
    pro = int(pro)
    d[name] = stu(name, pro=pro)
for j in range(M):
    name, mid = input().split()
    mid = int(mid)
    if name in d:
        d[name].mid = mid
    else:
        d[name] = stu(name, mid=mid)
for k in range(N):
    name, fin = input().split()
    fin = int(fin)
    if name in d:
        d[name].fin = fin
    else:
        d[name] = stu(name, fin=fin)

ql = [p for p in d.values() if p.isq()]
# qll = [p.record for p in ql]
# print(qll)
ql.sort(key=lambda x: x.record)
for p in ql:
    # print(p.record)
    print(p.name, p.pro, p.mid, p.fin, p.end)
