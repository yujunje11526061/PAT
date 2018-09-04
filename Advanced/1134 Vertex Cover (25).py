#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N,M = map(int, input().split())
# 以边为集合元素，直接通过集合的差集来判断，超时。
# table = [set() for i in range(N)]
# totset = set()
# for _ in range(M):
#     i,j = map(int, input().split())
#     table[i].update({(i,j),(j,i)})
#     table[j].update({(i,j),(j,i)})
#     totset.update({(i,j),(j,i)})
#
# K = int(input())
# for query in range(K):
#     num, *seq = map(int, input().split())
#     # tempset = totset.copy()
#     thisset = set()
#     for v in seq:
#         thisset.update(table[v])
#     if len(totset - thisset)>0:
#         print('No')
#     else:
#         print('Yes')

# 这样勉强过4个点，碰到超时题可以多提交几次看看
edgeset = set()
for _ in range(M):
    i,j = map(int, input().split())
    edgeset.add((i,j))

K = int(input())
for query in range(K):
    seq = map(int, input().split())
    next(seq)
    seq = set(seq)
    # tempset = set()
    flag = 1
    for i,j in edgeset:
        if i not in seq and j not in seq:
            print('No')
            flag = 0
            break
        # tempset.update({i,j})
        # if len(tempset) == N:
        #     break
    if flag:
        print('Yes')