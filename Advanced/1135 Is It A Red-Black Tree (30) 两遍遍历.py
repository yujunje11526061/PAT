#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
There is a kind of balanced binary search tree named red-black tree in the data structure. It has the following 5 properties:
(1) Every node is either red or black.
(2) The root is black.
(3) Every leaf (NULL) is black. 这点是关键啊，外部结点算黑色的，然后计算黑色高度的时候是算进去的！！不然碰到独臂一点都不平衡！！
(4) If a node is red, then both its children are black.
(5) For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.
对于这种只需要判断是不是的问题，直接弄个全局，发现不符合就改全局，然后有些步骤前通过全局来看要不要继续走
从而省去不必要的耗时。
把条件1，条件4，条件5分开来处理，免得混在一起搞不清楚。
'''
K = int(input())


class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_to_tree(s, e):
    if s > e:
        return
    if s == e:
        return node(pre[s])
    root = abs(pre[s])
    i, j = s + 1, e
    while i <= e:  # 从前往后扫，比根小的就是左子树
        if abs(pre[i]) <= root:
            i += 1
        else:
            break
    left = pre_to_tree(s + 1, i - 1)
    right = pre_to_tree(i, e)
    return node(pre[s], left, right)


def judge(t):
    global flag
    if not t:
        return 1  # 由题意，外部结点也算黑的！！！！！
    this = 1 if t.value > 0 else 0  # 此处结点为红为黑？黑为1
    count_left = judge(t.left)
    count_right = judge(t.right)
    if flag and count_left == count_right:  # flag 先判断，为0直接跳出了，否则下面返回了个None，None+int会有问题
        return count_left + this
    else:
        flag = 0
        return


def dfs(t):
    global flag
    # 本题外部结点算黑的，所以内部叶子结点是红的没事，反之，内部叶子节点就必须黑色了，不过红黑树本身就规定外部结点是黑色的
    if not t:
        return
    if flag and t.left:
        if t.value < 0 and t.left.value < 0:
            flag = 0
            return
        dfs(t.left)
    if flag and t.right:
        if t.value < 0 and t.right.value < 0:
            flag = 0
            return
        dfs(t.right)


for i in range(K):
    N = int(input())
    pre = list(map(int, input().split()))
    if pre[0] < 0:
        print('No')
        continue
    root = pre_to_tree(0, N - 1)
    flag = 1
    dfs(root)
    if flag:
        judge(root)
    if not flag:
        print('No')
    else:
        print('Yes')
