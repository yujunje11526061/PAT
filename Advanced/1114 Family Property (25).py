#!/usr/bin/env.python
# -*- coding:utf-8 -*-
class Family(): # 初始无房产
    def __init__(self, id):
        self.num = 1
        self.id = id
        self.stat = 0
        self.square = 0

root = [None] * 10000


def find_root(x):
    if root[x] is None:
        root[x] = Family(x)
        return x
    elif isinstance(root[x], Family):
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]


def union(a, b):
    ra, rb = find_root(a), find_root(b)
    if ra == rb:
        return
    elif ra < rb:
        fa, fb = root[ra], root[rb]
        fa.num += fb.num
        fa.stat += fb.stat
        fa.square += fb.square
        root[b], root[rb] = ra, ra
    else:
        fa, fb = root[ra], root[rb]
        fb.num += fa.num
        fb.stat += fa.stat
        fb.square += fa.square
        root[a], root[ra] = rb, rb

N = int(input())
for _ in range(N):
    i, fat,mot, numk,*seq = map(int, input().split())
    find_root(i)
    if fat != -1:
        union(i,fat)
    if mot != -1:
        union(i,mot)
    for son in seq[:numk]:
        union(i, son)
    # 把i拥有的房产归入所属家庭中
    fam = root[find_root(i)]
    fam.stat += seq[-2]
    fam.square += seq[-1]

l = [f for f in root if isinstance(f, Family)]
l.sort(key = lambda x:(-x.square/x.num, x.id))
print(len(l))
output = ['{:0>4} {} {:.3f} {:.3f}'.format(f.id, f.num, f.stat/f.num, f.square/f.num)
           for f in l]
print('\n'.join(output))
# for f in l:
#         print('{:0>4} {} {:.3f} {:.3f}'.format(f.id, f.num, f.stat/f.num, f.square/f.num))