#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import deque

M, N = map(int, input().split())
io = list(map(int, input().split()))
locationInIo = {io[i]: i for i in range(N)}
pre = list(map(int, input().split()))

class node():
    def __init__(self, key, loc=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.loc = loc


# build tree
q = deque([])
q.append([0, N - 1, 0, N - 1, None, None])
finalroot = None
while (len(q) > 0):
    si, ei, sp, ep, fa, flag = q.popleft()
    if si <= ei:
        root = pre[sp]
        thisnode = node(root,loc=locationInIo[root])
        if finalroot is None:
            finalroot = thisnode
        if flag == 0:
            fa.left = thisnode
        elif flag == 1:
            fa.right = thisnode

        location = locationInIo[root]
        length = location - si
        forLeft = [si, si + length - 1, sp + 1, sp + length, thisnode, 0]
        forRight = [si + length + 1, ei, sp + length + 1, ep, thisnode, 1]
        q.append(forLeft)
        q.append(forRight)

def check(u,v,root = finalroot):
    if u not in locationInIo and v not in locationInIo:
        print(f"ERROR: {u} and {v} are not found.")
        return
    elif u not in locationInIo or v not in locationInIo:
        x = u if u not in locationInIo else v
        print(f"ERROR: {x} is not found.")
        return
    else:
        locu,locv = locationInIo[u],locationInIo[v]
        while(root):
            if u==root.key:
                print(f"{u} is an ancestor of {v}.")
                return
            elif v == root.key:
                printf(f"{v} is an ancestor of {u}.")
                return
            elif locu<root.loc and locv<root.loc:
                root = root.left
            elif locu>root.loc and locv>root.loc:
                root = root.right
            else:
                print(f"LCA of {u} and {v} is {root.key}.")
                return

for _ in range(M):
    u,v = map(int, input().split())
    check(u,v)
