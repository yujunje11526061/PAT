#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
已知二叉搜索树的前（后）序遍历，排序可以求出中序遍历
但是注意，不同于一般的已知两序求另一序，一般情况下给的时节点编号，不会重复。
二叉搜索树的值会重复（有些题意时这么定义的，相等的放左边或右边）
此时你在用.index()方法去找中序中的下标时会错误。
故如果要用常规两序求第三序的方法，应对前（后）序中的数据编号，作为排序的第二项指标。使得满足题意指定的先后关系
例如本题，相等的去右边，非镜像时，前序中先出的，中序中也先出，镜像时，前序中先出的中序中后出

更优的做法：充分利用二叉搜索树的性质，数据时按照大小关系分类的！见本题的改进算法。
也不用在过程中去判断镜像与非镜像，容易写错，直接假定时其中一种，去判断是否满足。
'''

n = int(input())
l = list(map(int, input().split()))


def judge(s, e):
    global flag
    if s >= e:
        return True
    center = l[s]
    i = s + 1
    if (l[i] < center and l[e] < center) or (l[i] >= center and l[e] >= center):
        return judge(i, e)
    elif l[i] < center and l[e] >= center:  # 非镜像中找 flag：False
        if flag is None or flag == False:
            flag = False
            while i <= e:
                if l[i] < center:
                    i += 1
                else:
                    break
            j = i
            while i <= e:
                if l[i] >= center:
                    i += 1
                else:
                    return False
            return judge(s + 1, j - 1) and judge(j, e)
        else:
            return False

    else:  # 镜像中找 flag：True
        if flag is None or flag == True:
            flag = True
            while i <= e:
                if l[i] >= center:
                    i += 1
                else:
                    break
            j = i
            while i <= e:
                if l[i] < center:
                    i += 1
                else:
                    return False
            return judge(s + 1, j - 1) and judge(j, e)
        else:
            return False


def to_postorder(si, ei, sp, ep):
    global seq
    if si == ei:
        seq.append(li[si][0])
        return
    elif si>ei:
        return
    root = l[sp]
    p = li.index(root)
    length = p - si
    to_postorder(si, si + length - 1, sp + 1, sp + length)
    to_postorder(si + length + 1, ei, sp + length + 1, ep)
    seq.append(root[0])


flag = None
seq = []
if len(l) == 1:
    print('YES')
    print(l[0])
elif judge(0, n - 1):
    print('YES')
    if flag:  # 镜像的
        l = [(l[i],i) for i in range(n)] # 为了处理有相同值的情况，镜像下，前序中先出的中序中后出，因为后面有reverse，所以仍然时前序在前的序号小
        li = sorted(l, reverse=True)  # 中序遍历
        to_postorder(0, n - 1, 0, n - 1)
        print(*seq)
    else:
        l = [(l[i], i) for i in range(n)] # 为了处理有相同值的情况，非镜像下，前序中先出的中序中也先出
        li = sorted(l)
        to_postorder(0, n - 1, 0, n - 1)
        print(*seq)
else:
    print('NO')
