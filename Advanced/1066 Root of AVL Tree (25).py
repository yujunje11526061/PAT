#!/usr/bin/env.python
# -*- coding:utf-8 -*-
def ll(a):
    b = a.left
    a.left = b.right
    b.right = a
    a.bf = b.bf = 0
    return b


def rr(a):
    b = a.right
    a.right = b.left
    b.left = a
    a.bf = b.bf = 0
    return b


def lr(a, b):
    c = b.right
    a.left = c.right
    b.right = c.left
    c.left, c.right = b, a
    if c.bf == 0:
        a.bf = b.bf = 0
    elif c.bf > 0:
        b.bf = 0
        a.bf = -1
    else:
        b.bf = 1
        a.bf = 0
    c.bf = 0
    return c


def rl(a, b):
    c = b.left
    a.right = c.left
    b.left = c.right
    c.left,c.right = a,b
    if c.bf == 0:
        a.bf = b.bf =0
    elif c.bf >0:
        a.bf = 0
        b.bf = -1
    else:
        a.bf = 1
        b.bf = 0
    c.bf = 0
    return c


class node():
    def __init__(self, key, left=None, right=None, bf=0):
        self.key = key
        self.left = left
        self.right = right
        self.bf = bf


n = int(input())
l = map(int, input().split())
t = None
for x in l:
    if t is None:
        t = node(x)
        continue
    p = a = t
    pp = pa = None
    while p is not None:
        if p.bf != 0:
            a = p
            pa = pp
        if x < p.key:
            pp = p
            p = p.left
        else:
            pp = p
            p = p.right
    if x < pp.key:
        pp.left = node(x)
    else:
        pp.right = node(x)

    p = a
    while p.key != x:
        if x < p.key:
            p.bf += 1
            p = p.left
        else:
            p.bf -= 1
            p = p.right
    nt = t
    if a.bf == 2:
        b = a.left
        if b.bf == 1:
            nt = ll(a)
        else:
            nt = lr(a, b)
    elif a.bf == -2:
        b = a.right
        if b.bf == -1:
            nt = rr(a)
        else:
            nt = rl(a, b)

    if pa is None:
        t = nt
    elif nt.key < pa.key:
        pa.left = nt
    else:
        pa.right = nt

print(t.key)
