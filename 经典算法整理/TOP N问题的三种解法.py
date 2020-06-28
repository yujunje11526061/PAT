#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import time
from collections import OrderedDict


class Partition:
    '''
    二分查找与快排思想的结合
    '''

    @classmethod
    def find(cls, seq: list, N: int) -> list:
        cls.seq = list(seq)
        cls.N = N
        cls.flag = 0
        if len(seq) == 0 or N > len(seq) or N <= 0:
            return 'Bad seq or bad N'
        cls.partition(0, len(seq) - 1)
        return sorted(cls.seq[:N])

    @classmethod
    def partition(cls, s, e):
        if cls.flag == 1 or s >= e:
            return
        pivot = cls.seq[e]
        i, j = s, e - 1
        while i < j:
            while cls.seq[i] < pivot:
                i += 1
            while cls.seq[j] > pivot:
                j -= 1
            if i < j:
                cls.seq[i], cls.seq[j] = cls.seq[j], cls.seq[i]

        cls.seq[i], cls.seq[e] = cls.seq[e], cls.seq[i]
        if i == cls.N:
            cls.flag = 1
            return
        elif i < cls.N:
            cls.partition(i + 1, e)
        else:
            cls.partition(s, j)


class SearchTree:
    '''
    基于平衡二叉搜索树实现，其实如果只是topN的话，普通搜索树就行了
    中序遍历的前N个
    '''

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class AVLTree:
        def __init__(self, root=None, balance=True):
            self.root = root
            self.balance = balance

        def topN(self, N):
            self.top_n_list = []

            def topNtraversal(node):
                nonlocal N
                if N == 0 or node is None:
                    return
                topNtraversal(node.left)
                if N == 0:
                    return
                N -= 1
                self.top_n_list.append(node.val)
                topNtraversal(node.right)

            topNtraversal(self.root)
            return self.top_n_list

        def insert(self, x: int):
            if self.root is None:
                self.root = SearchTree.Node(x)
            else:
                p = self.root
                pp = None
                while p is not None:
                    pp = p
                    if p.val >= x:
                        p = p.left
                    else:
                        p = p.right
                if pp.val >= x:
                    pp.left = SearchTree.Node(x)
                else:
                    pp.right = SearchTree.Node(x)

            if self.balance:
                _, self.root, __ = self.getHeightAndRoot(self.root)

        def LL_Rotate(self, node):
            l = node.left
            node.left = l.right
            l.right = node
            return l

        def LR_Rotate(self, node):
            node.left = self.RR_Rotate(node.left)
            return self.LL_Rotate(node)

        def RR_Rotate(self, node):
            r = node.right
            node.right = r.left
            r.left = node
            return r

        def RL_Rotate(self, node):
            node.right = self.LL_Rotate(node.right)
            return self.RR_Rotate(node)

        def getHeightAndRoot(self, node):
            '''
            :param node:
            :return: (自身高度，当前树根，左子树高度-右子树高度)
            '''
            if node is None:
                return (0, None, 0)
            leftHeight, leftRoot, leftFlag = self.getHeightAndRoot(node.left)
            rightHeight, rightRoot, rightFlag = self.getHeightAndRoot(node.right)
            node.left, node.right = leftRoot, rightRoot
            if leftHeight - rightHeight > 1:
                if leftFlag == 1:
                    newRoot = self.LL_Rotate(node)
                else:
                    newRoot = self.LR_Rotate(node)
                return (leftHeight + rightHeight) // 2 + 1, newRoot, 0
            elif leftHeight - rightHeight < -1:
                if rightFlag == -1:
                    newRoot = self.RR_Rotate(node)
                else:
                    newRoot = self.RL_Rotate(node)
                return (leftHeight + rightHeight) // 2 + 1, newRoot, 0
            else:
                return max(leftHeight, rightHeight) + 1, node, leftHeight - rightHeight

    @classmethod
    def find(cls, seq: list, N: int) -> list:
        cls.seq = list(seq)
        cls.N = N
        tree = cls.AVLTree(balance=True)
        for i in seq:
            tree.insert(i)
        return tree.topN(N)


class MaxHeap:
    '''
    最大堆管理当前最小的N个数，新插入的数大于堆顶就不可能是TopN小
    '''

    @classmethod
    def find(cls, seq: list, N: int) -> list:
        cls.seq = list(seq)
        cls.N = N
        cls.flag = 0
        if len(seq) == 0 or N > len(seq) or N <= 0:
            return 'Bad seq or bad N'

        cls.maxheap = []
        for i in cls.seq:
            cls.insert(i)
        return sorted(cls.maxheap)

    @classmethod
    def insert(cls, x: int):
        if not isinstance(cls.__dict__.get('maxheap'), list):
            cls.maxheap = []
        if cls.__dict__.get('N'):
            cls.N = 10

        def replaceHead(x):
            i, j = 0, 1
            while j < cls.N:
                if j + 1 < cls.N and cls.maxheap[j + 1] > cls.maxheap[j]:
                    j += 1
                if x >= cls.maxheap[j]:
                    break
                else:
                    cls.maxheap[i] = cls.maxheap[j]
                    i, j = j, 2 * j + 1
            cls.maxheap[i] = x

        def siftUp(x):
            cls.maxheap.append(None)
            i = len(cls.maxheap) - 1
            j = (i - 1) // 2
            while i > 0:
                if x <= cls.maxheap[j]:
                    break
                else:
                    cls.maxheap[i] = cls.maxheap[j]
                    i, j = j, (j - 1) // 2
            cls.maxheap[i] = x

        if len(cls.maxheap) >= cls.N and x < cls.maxheap[0]:
            replaceHead(x)

        elif len(cls.maxheap) < cls.N:
            siftUp(x)


N = 1000
R = 1000000
r = 5
C = 2
t0 = time.time()
for i in range(C):
    l = list(range(R)) + list(range(r))
    random.shuffle(l)
    # print(Partition.find(l, N))

print("\n\n")
t1 = time.time()

for i in range(C):
    l = list(range(R)) + list(range(r))
    random.shuffle(l)
    # print(SearchTree.find(l, N))

print("\n\n")
t2 = time.time()

for i in range(C):
    l = list(range(R)) + list(range(r))
    random.shuffle(l)
    # print(MaxHeap.find(l, N))

print("\n\n")
t3 = time.time()

print("\n\n")
print(f"Partition: {(t1-t0)*1000}ms\nSearchTree: {(t2-t1)*1000}ms\nMaxHead: {(t3-t2)*1000}ms")