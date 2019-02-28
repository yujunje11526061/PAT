#!/usr/bin/env python
# -*- coding:utf-8 -*-
N = int(input())
l = map(int,input().split())

class node():
    def __init__(self,key):
        self.key =key
        self.height = 1
        self.left = None
        self.right = None



def getHeight(cnt:node): # 递归得到树高。不能取height属性。因为插入后实际树高和属性不服，需要用此法更新树高。
    if cnt is None:
        return 0
    else:
        return cnt.height

def singleLeftRotation(a:node)->node:
    b = a.left
    a.left = b.right
    b.right = a
    # getHeight用于取存储的高度属性，减少重复计算，减少求高度的开销，max()+1是更新操作，每次树发生变化相关节点都要记得更新。
    # 此处旋转后的低节点应先更新
    a.height =  max(getHeight(a.left), getHeight(a.right)) + 1
    b.height =  max(getHeight(b.left), getHeight(b.right)) + 1
    return b

def singleRightRotation(a:node)->node:
    b = a.right
    a.right = b.left
    b.left = a
    a.height = max(getHeight(a.left), getHeight(a.right)) + 1
    b.height = max(getHeight(b.left), getHeight(b.right)) + 1
    return b

def doubleLeftRightRotation(a):
    b = a.left
    a.left = singleRightRotation(b)
    return singleLeftRotation(a)

def doubleRightLeftRotation(a):
    b = a.right
    a.right = singleLeftRotation(b)
    return singleRightRotation(a)

def insert( x:node,root:node)->"返回新的树根":
    if root is None:
        root = x
    elif x.key<root.key:
        root.left = insert(x, root.left)
        if getHeight(root.left)-getHeight(root.right)==2:  # 用getHeight函数是为处理空节点，直接取属性就报错了
            if(x.key<root.left.key):
                root = singleLeftRotation(root)
            else:
                root = doubleLeftRightRotation(root)
    else:
        root.right = insert(x, root.right)
        if getHeight(root.left)-getHeight(root.right) == -2:
            if(x.key<root.right.key):
                root = doubleRightLeftRotation(root)
            else:
                root = singleRightRotation(root)
    # getHeight用于取存储的高度属性，减少重复计算，减少求高度的开销，max()+1是更新操作，每次树发生变化都要记得更新。
    root.height = max(getHeight(root.left), getHeight(root.right)) + 1
    return root

root =None
for data in l:
    root = insert(node(data),root)

print(root.key)