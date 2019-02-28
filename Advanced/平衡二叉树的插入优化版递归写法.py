#!/usr/bin/env python
# -*- coding:utf-8 -*-
N = int(input())
l = map(int,input().split())

class SearchTree:
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
            pass

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
            node.left, node.right = leftRoot, rightRoot # 记得更新左右子树
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

root =None
tree = SearchTree.AVLTree()
for data in l:
    tree.insert(data)
    # print(tree.root.val)


print(tree.root.val)