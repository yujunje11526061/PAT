#!/usr/bin/env python
# -*- coding:utf-8 -*-
N = int(input())
l = map(int,input().split())

class node():
    def __init__(self,key):
        self.key =key
        # self.height = 1 # 此属性其实没用，可以没有。
        self.left = None
        self.right = None



def getHeight(cnt:node): # 递归得到树高。不能取height属性。因为插入后实际树高和属性不服，需要用此法更新树高。
    if cnt is None:
        return 0
    else:
        return max(getHeight(cnt.left),getHeight(cnt.right))+1

def singleLeftRotation(a:node)->node:
    b = a.left
    a.left = b.right
    b.right = a
    # a.height =  getHeight(a)
    # b.height =  getHeight(b)
    return b

def singleRightRotation(a:node)->node:
    b = a.right
    a.right = b.left
    b.left = a
    # a.height = getHeight(a)
    # b.height = getHeight(b)
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
        if getHeight(root.left)-getHeight(root.right)==2:  # 插入后高度变化了。此处不能取height属性。而应该用getHeight函数
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
    # root.height = max(root.left.height,root.right.height)+1
    return root

root =None
for data in l:
    root = insert(node(data),root)

print(root.key)