#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
根据中前(后)序遍历递归建树,注意递归终止条件和递归区间. 背下来!
来回往返的层序遍历, 用两个堆栈,交替用.
'''

n = int(input())
io = list(map(int, input().split()))
po = list(map(int, input().split()))


class T():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_root(si, ei, sp, ep):
    if si > ei:
        return
    if si == ei:
        return T(io[si])
    root = po[ep]
    index = io.index(root)
    l = index - si
    left = find_root(si, si + l - 1, sp, sp + l - 1)
    right = find_root(si + l + 1, ei, sp + l, ep - 1)
    return T(root, left, right)


def preorder(t):
    if t is not None:
        print(t.value)
        preorder(t.left)
        preorder(t.right)


t = find_root(0, n - 1, 0, n - 1)
# preorder(t)
from collections import deque

stack = [t]
stack2 = []
queue = deque()
docker = []
# i = False
while len(stack) > 0 or len(stack2) > 0:

    while len(stack) > 0:
        p = stack.pop()
        docker.append(p.value)
        if p.right is not None:
            stack2.append(p.right)
        if p.left is not None:
            stack2.append(p.left)

    while len(stack2) > 0:
        p = stack2.pop()
        docker.append(p.value)
        if p.left is not None:
            stack.append(p.left)
        if p.right is not None:
            stack.append(p.right)

print(*docker)
