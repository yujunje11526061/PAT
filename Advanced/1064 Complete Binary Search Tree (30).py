#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
熟练分析二叉树的结构特征，完全二叉树的节点数目特征
递归的熟练使用，递归出口的处理，新递归条件的处理。
排序得到BST的中序序列。通过CST的结构特征可以知道根的下标。
'''
import math
from collections import deque
N = int(input())
l = sorted(map(int, input().split()))
class node():
    def __init__(self,value, left=None,right = None):
        self.value = value
        self.left = left
        self.right = right

def do(s,e):
    if s>e:
        return
    if s == e:
        return node(l[s])
    n = e-s+1
    # print(n)
    layer = math.ceil(math.log(n+1,2))
    max_num_of_last_layer = 2**(layer) - 2**(layer-1)
    num_of_last_layer = n-2**(layer-1)+1
    if num_of_last_layer <= max_num_of_last_layer//2: # 最后一层只填根的左子树
        nright = (n-1-num_of_last_layer)//2
        nleft = n-1-nright
        root = l[s+nleft]
    else:
        nleft = (2**layer-1-1)//2
        nright = n-1-nleft
        root = l[s+nleft]
    left = do(s,s+nleft-1)
    right = do(s+nleft+1, e)
    return node(root,left,right)

def level_order_traversal(T):
    queue = deque([T])
    ll = []
    while len(queue)>0:
        p = queue.popleft()
        ll.append(p.value)
        if p.left is not None:
            queue.append(p.left)
        if p.right is not None:
            queue.append(p.right)
    return ll

if N == 1:
    print(l[0])
else:
    T = do(0,N-1)
    ll = level_order_traversal(T)
    print(*ll)
