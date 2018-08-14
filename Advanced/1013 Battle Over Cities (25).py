#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
本题为图的遍历，并求连通集的个数
'''
N,M,K = map(int, input().split())
table = [[] for i in range(N)]

for _ in range(M):
    i,j = map(int, input().split())
    i, j = i-1, j-1
    table[i].append(j)
    table[j].append(i)

need_to_check = map(int, input().split()) # 编号大一号

for i in need_to_check:
    i = i-1
    st = set(range(N))
    st.remove(i)
    ll = []
    while len(st) > 0:
        s = set()
        stack = [st.pop()]
        while len(stack)>0:
            p = stack.pop()
            if p not in s:
                s.add(p)
                for j in table[p]:
                    if j in st and j != i:
                        st.remove(j)
                        stack.append(j)
        ll.append(s)
    print(len(ll)-1)
