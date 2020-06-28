#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
也可以用一个伪单调栈，但是新元素小于栈顶且栈顶计数>1就弹出，因为栈顶可能计数为1，所以不能弹出，于是此处不单调，故是一个分段单调增的栈，最后栈底的就是最小的首字母。

'''
from collections import defaultdict, deque

seq = input()
d = defaultdict(lambda: 0)
newseq = []
for i in seq:
    if i.isalpha():
        i = i.lower()
        newseq.append(i)
        d[i] = d[i] + 1

q = deque([])
minX = newseq[0]
for i in newseq:
    q.append(i)
    # 比当前值大，且计数大于1的肯定不可能为队首，直接弹出
    # 最后剩下的元素是计数为1或者计数大于1但是值更小的，他们都可能成为最终的最小
    while len(q) > 1 and d[q[0]] > 1 and i <= q[0]:
        d[q.popleft()] -= 1


    if q[0] < minX: # 双端队列法需要每次都与曾经最小的去比，得最终最小
        minX = q[0]

print(minX)
