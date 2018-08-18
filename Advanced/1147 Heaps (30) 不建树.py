#!/usr/bin/env.python
# -*- coding:utf-8 -*-
def judge_heap(T):
    if T[0]>T[1]: # 看是否最大堆
        for i in range(n):
            if 2*i+1 < n and T[i] < T[2*i+1]:
                return 'Not Heap'
            if 2*i+2 < n and T[i] < T[2*i+2]:
                return 'Not Heap'
        return 'Max Heap'
    else: # 看是否最小堆
        for i in range(n):
            if 2*i+1 < n and T[i] > T[2*i+1]:
                return 'Not Heap'
            if 2*i+2 < n and T[i] > T[2*i+2]:
                return 'Not Heap'
        return 'Min Heap'


def post_order_recv(i):
    global dk
    if i>n-1:
        return
    post_order_recv(2*i+1)
    post_order_recv(2*i+2)
    dk.append(tree[i])

M, N = map(int, input().split())
for i in range(M):
    tree  = list((map(int, input().split())))
    n = len(tree)
    print(judge_heap(tree))
    dk = []
    post_order_recv(0)
    print(*dk)