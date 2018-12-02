#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import deque

M, N = map(int, input().split())
io = list(map(int, input().split()))
locationInIo = {io[i]: i for i in range(N)}
pre = list(map(int, input().split()))


class node():
    def __init__(self, key, fa=None, left=None, right=None):
        self.key = key
        self.fa = fa
        self.left = left
        self.right = right


si, ei, sp, ep = 0, N - 1, 0, N - 1
# build tree
tree = []
q = deque([])
q.append([0, N - 1, 0, N - 1, None, None])
while (len(q) > 0):
    si, ei, sp, ep, fa, flag = q.popleft()
    if si <= ei:
        root = pre[sp]
        thisnode = node(root)
        if flag == 0:
            fa.left = thisnode
            thisnode.fa = fa
        elif flag == 1:
            fa.right = thisnode
            thisnode.fa = fa

        location = locationInIo[root]
        length = location - si
        tree.append(thisnode)
        forLeft = [si, si + length - 1, sp + 1, sp + length, tree[-1], 0]
        forRight = [si + length + 1, ei, sp + length + 1, ep, tree[-1], 1]
        q.append(forLeft)
        q.append(forRight)

tree.sort(key=lambda t: t.key)


def binarySearch(l, p):
    s, e = 0, len(l)-1
    while 0<=s <= e<=len(l)-1:
        mid = (s + e) // 2
        if l[mid].key < p:
            s = mid + 1
        elif l[mid].key > p:
            e = mid - 1
        else:
            return tree[mid]
    return False


def check(u, v):
    nodeu = binarySearch(tree, u)
    nodev = binarySearch(tree, v)
    if nodeu is False and nodev is False:
        print(f"ERROR: {u} and {v} are not found.")
        return
    elif nodeu is False or nodev is False:
        x = u if nodeu is False else v
        print(f"ERROR: {x} is not found.")
        return
    else:
        pathu = set()
        pathv = set()
        pu, pv = nodeu, nodev
        while pu or pv:
            if pu:
                if pu.key in pathv:
                    if pu.key==v:
                        print(f"{v} is an ancestor of {u}.")
                    else:
                        print(f"LCA of {u} and {v} is {pu.key}.")
                    return
                pathu.add(pu.key)
                pu = pu.fa
            if pv:
                if pv.key in pathu:
                    if pv.key == u:
                        print(f"{u} is an ancestor of {v}.")
                    else:
                        print(f"LCA of {u} and {v} is {pv.key}.")
                    return
                pathv.add(pv.key)
                pv = pv.fa

for _ in range(M):
    u, v = map(int, input().split())
    check(u, v)