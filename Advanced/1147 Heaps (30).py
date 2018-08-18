#!/usr/bin/env.python
# -*- coding:utf-8 -*-

class Node():
    def __init__(self, value = None, left = None, right = None, father= None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(l):
    l = list(l)
    tree = []
    for i in range(len(l)):
        node = Node(l[i])
        tree.append(node)
        if i > 0: # 有父节点
            father = (i-1)//2
            if (i-1)%2 == 0: # 左孩子
                tree[father].left = node
            else:
                tree[father].right = node
    return tree

def judge_heap(T):
    if T[0].value>T[1].value: # 看是否最大堆
        for t in T:
            if t.left is not None and t.value <= t.left.value:
                return 'Not Heap'
            if t.right is not None and t.value <= t.right.value:
                return 'Not Heap'
        return 'Max Heap'
    else: # 看是否最小堆
        for t in T:
            if t.left is not None and t.value >= t.left.value:
                return 'Not Heap'
            if t.right is not None and t.value >= t.right.value:
                return 'Not Heap'
        return 'Min Heap'

def post_order(T):
    t = T[0]
    stack = []
    docker = []
    while t is not None or len(stack) > 0:
        while t is not None:
            stack.append(t)
            t = t.left if t.left is not None else t.right
        t = stack.pop()
        docker.append(t.value)
        if len(stack)>0:
            x = stack[-1]
            if x.left is t:
                t = x.right
            else:
                t = None
        else:
            t = None
    return docker

def post_order_recv(t):
    global dk
    if t is None:
        return
    post_order_recv(t.left)
    post_order_recv(t.right)
    dk.append(t.value)

M, N = map(int, input().split())
for i in range(M):
    tree = build_tree(map(int, input().split()))
    print(judge_heap(tree))
    # print(*post_order(tree))
    dk = []
    post_order_recv(tree[0])
    print(*dk)