#!/usr/bin/env.python
# -*- coding:utf-8 -*-
M, N, K = map(int, input().split())

def do():
    seq = list(range(N, 0, -1))
    stack = []
    l = map(int, input().split())
    for j in l:
        while len(seq) > 0 and seq[-1] <= j:
            stack.append(seq.pop())
            if len(stack) > M:
                return 'NO'

        if len(stack) > 0 and stack[-1] == j:
            stack.pop()
        else:
            return 'NO'
    return 'YES'


for i in range(K):
    print(do())