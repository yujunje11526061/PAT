#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
 利用好默认字典
 并查集规范写法，看1118
'''
from collections import defaultdict

d = defaultdict(lambda: 0)
dfather = defaultdict(lambda :None)
N = int(input())
record = []

def find_father(id):
    if dfather[id]>=0:
        dfather[id] = find_father(dfather[id]) # 路径压缩
        return dfather[id]
    else:
        return id

def find_cluster(this, myhobby):
    for i in range(len(record)):  # 要把每个人都遍历一遍，防止新人作为两个团体的桥梁这种情况时，团体间归并被遗漏。
        i_hobby = set(record[i])
        for mh in myhobby:
            if mh in i_hobby:
                if dfather[this] is None:
                    dfather[this] = find_father(i)
                    dfather[dfather[this]] -= 1
                else:
                    f1, f2 = find_father(this), find_father(i)
                    if f1 == f2:
                        break
                    n1 ,n2 = dfather[f1], dfather[f2]
                    if n1<= n2:
                        dfather[f2] = f1
                        dfather[f1] = n1+n2
                        be_father.remove(f2)
                        be_father.add(f1)
                    else:
                        dfather[f1] = f2
                        dfather[f2] = n1+n2
                        be_father.remove(f1)
                        be_father.add(f2)
                break
    if dfather[this] is None:
        dfather[this] = -1
        be_father.add(this)
    return

be_father = set()
for this in range(N):
    myhobby = input().split()[1:]
    myhobby = list(map(int, myhobby))
    find_cluster(this, myhobby)
    record.append(myhobby)

count = len(be_father)
l = sorted([-dfather[every] for every in be_father], reverse=True)
print(count)
print(*l)

