#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
已知二叉搜索树的前（后）序遍历，排序可以求出中序遍历
但是注意，不同于一般的已知两序求另一序，一般情况下给的时节点编号，不会重复。
二叉搜索树的值会重复（有些题意时这么定义的，相等的放左边或右边）
此时你在用.index()方法去找中序中的下标时会错误。
故如果要用常规两序求第三序的方法，应对前（后）序中的数据编号，作为排序的第二项指标。使得满足题意指定的先后关系
例如本题，相等的去右边，非镜像时，前序中先出的，中序中也先出，镜像时，前序中先出的中序中后出

更优的做法：充分利用二叉搜索树的性质，直接前后序转换，不用中序了。
也不用在过程中去判断镜像与非镜像，容易写错，直接假定时其中一种，去判断是否满足。
'''

n = int(input())
pre = list(map(int, input().strip().split()))


def to_post(s, e):
    if s > e:
        return
    root = pre[s]
    i, j = s + 1, e
    if isMirror:
        while i <= e and pre[i] >= root:
            i += 1
        while j > s and pre[j] < root:
            j -= 1
    else:
        while i <= e and pre[i] < root:
            i += 1
        while j > s and pre[j] >= root:
            j -= 1

    if i - j != 1:
        return
    to_post(s + 1, j)
    to_post(i, e)
    post.append(root)


isMirror = False
post = []
to_post(0, n - 1)
if len(post) < n:
    post = []
    isMirror = True
    to_post(0, n - 1)
if len(post) < n:
    print('NO')
else:
    print('YES')
    print(*post)
