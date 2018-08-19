#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
由后序遍历和中序遍历求层序遍历
'''

n = int(input())  # <= 30,, 不同的正整数
postorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))


class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_root(si, ei, sp, ep):  # ep-sp == ei-si
    if si > ei:
        return None
    if si == ei:
        return node(inorder[si])
    root = postorder[ep]
    index = inorder.index(root)
    l = index - si  # 求出左子树的长度
    # 关键在于递归时区间的计算，依据是同一子树长度相等
    left = find_root(si, index - 1, sp, sp + l - 1)
    right = find_root(index + 1, ei, sp + l, ep - 1)
    return node(root, left, right)


T = find_root(0, n - 1, 0, n - 1)

from collections import deque

queue = deque()
q = []

while T is not None:
    q.append(T.value)
    if T.left is not None:
        queue.append(T.left)
    if T.right is not None:
        queue.append(T.right)
    if len(queue) > 0:
        T = queue.popleft()
    else:
        break

print(*q)
