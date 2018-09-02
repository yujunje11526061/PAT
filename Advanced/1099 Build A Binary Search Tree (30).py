#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
把编号当作key，读取key的时候就可以建树。然后对树中序遍历。对应的value从小到大排，其必然一一对应地填入中序遍历中
取排序后的value列表的迭代器，则在中序遍历树的过程中可以直接填入，不需要遍历完再去走一遍来填充，减少一次列表扫描。
'''
from collections import deque
class node():
    def __init__(self,key, left,right,value= None ):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

N = int(input())
l = []

for key in range(N):
    left, right = map(int,input().split())
    l.append(node(key, left,right))

V = sorted(map(int, input().split()))
it = iter(V)

def inorder(t):
    if t == -1:
        return
    item = l[t]
    inorder(item.left)
    item.value = next(it)
    inorder(item.right)

inorder(0)
queue = deque([0])
outputlist = []
while len(queue)>0:
    p = queue.popleft()
    item = l[p]
    outputlist.append(item.value)
    left = item.left
    right = item.right
    if left != -1:
        queue.append(left)
    if right != -1:
        queue.append(right)

print(*outputlist)
