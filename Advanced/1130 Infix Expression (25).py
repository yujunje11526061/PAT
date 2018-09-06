#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
二叉树表示计算顺序，中序遍历就是中缀表达式，一个子树代表这个子树先做，意味着中缀表达式中有()来强调优先级的
(1+2)+3和1+(2+3)在中缀表达式中是不同意义的（虽然加法结合律指明值相等），但是体现在二叉树上是不一样的
注意递归的形式！！
'''


class node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


n = int(input())
nodelist = [None] * (n + 1)
ss = set(range(1, n + 1))
for i in range(1, n + 1):
    value, l, r = input().strip().split()
    l, r = int(l), int(r)
    ss.discard(l)
    ss.discard(r)
    nodelist[i] = node(value, l, r)

root = ss.pop()

sout = ''


def inorder(t):
    global sout
    value = nodelist[t].value
    l = nodelist[t].left
    r = nodelist[t].right
    if l != -1 and r != -1:
        sout += '('
        inorder(l)
        sout += value
        inorder(r)
        sout += ')'
    elif l != -1 and r == -1:
        sout += '('
        inorder(l)
        sout += value
        sout += ')'
    elif l == -1 and r != -1:
        sout += '('
        sout += value
        inorder(r)
        sout += ')'
    else:
        sout += value


if n == 1:
    print(nodelist[root].value)
else:
    inorder(root)
    print(sout[1:-1])
