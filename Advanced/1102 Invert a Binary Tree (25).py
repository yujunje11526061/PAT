#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import deque
N = int(input())
class node():
    def __init__(self, key, left= None, right=None):
        self.key = key
        self.left =left
        self.right = right

all_node = []
s = set(range(N))
for i in range(N):
    right, left = input().split()
    if right == '-':
        right = None
    else:
        right = int(right)
        s.remove(right)
    if left == '-':
        left = None
    else:
        left = int(left)
        s.remove(left)
    all_node.append(node(i, left,right))

level_order = []
in_order = []
root = s.pop()
queue = deque([root])
while len(queue)>0:
    item = all_node[queue.popleft()]
    if item.left is not None:
        queue.append(item.left)
    if item.right is not None:
        queue.append(item.right)
    level_order.append(item.key)

stack = []
t = root
while t is not None or len(stack)>0:
    while t is not None:
        stack.append(t)
        t = all_node[t].left
    t = stack.pop()
    in_order.append(all_node[t].key)
    t = all_node[t].right

print(*level_order)
print(*in_order)