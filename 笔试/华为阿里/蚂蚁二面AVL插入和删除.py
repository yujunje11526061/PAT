#!/usr/bin/env python
# -*- coding:utf-8 -*-
# / *
# *实现一个平衡二叉搜索树数据结构，并实现add操作
# * /

class Node():
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.count = 1


class Tree():
    '''
    没有重复元素，插入重复的不操作或者通过计数的方式
    '''

    def __init__(self, root=None):
        self.root = root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            p = self.root
            pp = None
            while p is not None:
                if p.key == key:
                    p.count += 1
                    return
                elif p.key < key:
                    pp = p
                    p = p.right
                else:
                    pp = p
                    p = p.left
            if pp.key < key:
                pp.right = Node(key)
            else:
                pp.left = Node(key)
        _, self.root, __ = self.adjustAndGetNewRoot(self.root)

    def delete(self, key):
        if self.root is None:
            return
        else:
            p = self.root
            pp = None
            while p is not None:
                # 搜索key的位置
                if p.key == key:
                    if p.count > 1:
                        p.count -= 1
                        return
                    else:
                        # 删除此节点并从左子树找个最大的或者右子树找个最小的替换他
                        # 找到记得修改父节点的指向，再跳出循环
                        # 还有种思路是不动节点，动里面的内容，把替换者和被替换者的内容交换下，然后删除被换下去的节点，这样只需注意两者有直接父子关系的情况，不用重新考虑和原树的连接
                        if pp is None:
                            # 要删除的p是根
                            flag = 0
                        elif pp.key > p.key:
                            # 要删除的p是pp的左子树
                            flag = -1
                        else:
                            # 要删除的p是pp的右子树
                            flag = 1
                        newp = Tree.delThisNode(p)
                        if flag == 0:
                            self.root = newp
                        elif flag == -1:
                            pp.left = newp
                        else:
                            pp.right = newp
                        break
                elif p.key < key:
                    pp = p
                    p = p.right
                else:
                    pp = p
                    p = p.left

            if p is None:
                # 本来就不在树中
                return
        # 成功删除记得调整平衡
        _, self.root, __ = self.adjustAndGetNewRoot(self.root)

    @staticmethod
    def delThisNode(node):
        '''
        选一个来替换他都那么多坑
        坑1：调用方删了根没更整个树的根
        坑2：选出来的跟要删除的是直接父子关系
        坑3：调用方在替换后没连到原来的树上
        '''
        if node.left is None and node.right is None:
            del node
            return None
        if node.left is not None:
            # 从左子树找最大的
            pp = None
            p = node.left
            while p.right is not None:
                pp = p
                p = p.right
            if pp is not None:
                pp.right = None

        else:
            # 从右子树找最小的
            pp = None
            p = node.right
            while p.left is not None:
                pp = p
                p = p.left
            if pp is not None:
                pp.left = None

        p.left = p.left if node.left is p else node.left
        p.right = p.right if node.right is p else node.right
        del node
        return p

    def singleL(self, node):
        a = node.left
        node.left = a.right
        a.right = node
        return a

    def singleR(self, node):
        a = node.right
        node.right = a.left
        a.left = node
        return a

    def doubleLR(self, node):
        a = node.left
        node.left = self.singleR(a)
        return self.singleL(node)

    def doubleRL(self, node):
        a = node.right
        node.right = self.singleL(a)
        return self.singleR(node)

    def adjustAndGetNewRoot(self, node) -> "当前子树的（高度，根, 左子树高度-右子树高度）元组":
        if node is None:
            return 0, None, 0
        else:
            leftHeight, leftRoot, diffLeft = self.adjustAndGetNewRoot(node.left)
            rightHeight, rightRoot, diffRight = self.adjustAndGetNewRoot(node.right)
            node.left, node.right = leftRoot, rightRoot
            newRoot = node

            if abs(leftHeight - rightHeight) <= 1:
                return max(leftHeight, rightHeight) + 1, newRoot, leftHeight - rightHeight

            elif leftHeight - rightHeight < -1:
                if diffRight < 0:
                    newRoot = self.singleR(node)
                else:
                    newRoot = self.doubleRL(node)
                return (leftHeight + rightHeight) // 2 + 1, newRoot, 0

            else:
                if diffLeft > 0:
                    newRoot = self.singleL(node)
                else:
                    newRoot = self.doubleLR(node)
                return (leftHeight + rightHeight) // 2 + 1, newRoot, 0

    def levelTraversal(self):
        from collections import deque

        if self.root is None:
            return
        q = deque([self.root])
        while len(q) > 0:
            thisNode = q.popleft()
            print(thisNode.key, end=" ")
            if thisNode.left is not None:
                q.append(thisNode.left)
            if thisNode.right is not None:
                q.append(thisNode.right)


tree = Tree()
for i in range(5, 0, -1):
    tree.insert(i)
    tree.levelTraversal()
    print("\n")

for i in range(6, 11):
    tree.insert(i)
    tree.levelTraversal()
    print("\n")

for i in range(5, 0, -1):
    tree.delete(i)
    tree.levelTraversal()
    print("\n")

for i in range(10, 5, -1):
    tree.delete(i)
    tree.levelTraversal()
    print("\n")

for i in range(1, 6):
    tree.insert(i)
    tree.levelTraversal()
    print("\n")

for i in range(1, 6):
    tree.delete(i)
    tree.levelTraversal()
    print("\n")
