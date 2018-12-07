#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import deque

# ll和rr写法相反，最后平衡因子都变成0
def ll(a, b):
    a.left = b.right
    b.right = a
    a.f = 0
    b.f = 0
    return b


def rr(a, b):
    a.right = b.left
    b.left = a
    a.f = 0
    b.f = 0
    return b

# lr和rl写法相反，两者的平衡因子调整都取决于c.f要分类讨论
def lr(a, b):
    c = b.right
    b.right = c.left
    c.left = b
    a.left = c.right
    c.right = a
    if c.f == 1:
        a.f = -1
        b.f = 0
    elif c.f == -1:
        a.f = 0
        b.f = 1
    else:
        b.f = 0
        a.f = 0
    c.f = 0
    return c


def rl(a, b):
    c = b.left
    b.left = c.right
    c.right = b
    a.right = c.left
    c.left = a
    if c.f == 1:
        a.f = 0
        b.f = -1
    elif c.f == -1:
        a.f = 1
        b.f = 0
    else:
        a.f = 0
        b.f = 0
    c.f = 0
    return c


class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.f = 0


N = int(input())
l = map(int, input().split())
root = None
for i in l:
    p, pp, a, pa = root, None, root, None
    if root is None:
        root = node(i)
        continue
    while p is not None:
        if p.f != 0:
            a = p
            pa = pp
        if i < p.value:
            pp = p
            p = p.left
        else:
            pp = p
            p = p.right
    if i < pp.value:
        pp.left = node(i)
    else:
        pp.right = node(i)

    # 沿路修改f因子
    cnt = a
    while cnt.value != i:
        if i < cnt.value:
            cnt.f += 1
            cnt = cnt.left
        else:
            cnt.f -= 1
            cnt = cnt.right
    # 调整，不用调整的情况下，局部根还是a，否则局部根由调整操作返回得到
    newroot = a
    if a.f == 2:
        b = a.left
        if i < b.value:
            newroot = ll(a, b)
        elif i > b.value:
            newroot = lr(a, b)
    elif a.f == -2:
        b = a.right
        if i > b.value:
            newroot = rr(a, b)
        elif i < b.value:
            newroot = rl(a, b)
    if pa is None: # a为总根的时候，记得更新总根
        root = newroot
    elif pa.value > newroot.value:
        pa.left = newroot
    else:
        pa.right = newroot

q = deque([root])
root.seq = 0
flag2 = 1
dock = []
while len(q) > 0:
    item = q.popleft()
    dock.append(item)
    # 其实可以更简单，一旦出现孩子为空的结点NoneArrise就标记为1，后面每次出现孩子为非空情况，看NoneArise是否已经为空了。若已经为空则不是完全二叉树。
    # 以完全二叉树的样子去编号，利用完全二叉树的编号特征这一知识点
    if item.left is not None and item.right is not None:
        item.left.seq = item.seq * 2 + 1
        item.right.seq = item.seq * 2 + 2
        q.extend([item.left, item.right])
    elif item.left is not None and item.right is None:
        item.left.seq = item.seq * 2 + 1
        q.append(item.left)
    elif item.left is None and item.right is not None:
        item.right.seq = item.seq * 2 + 2
        q.append(item.right)

# 如果是完全二叉树，则最后一个节点的编号应该为N-1
if N - 1 < dock[-1].seq:
    flag2 = 0
print(*[i.value for i in dock])
print('YES' if flag2 else 'NO')
