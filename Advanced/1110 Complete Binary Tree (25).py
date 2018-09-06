#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
和1123对比，完全二叉树判别法。
层序遍历时，以CBT的样子编号，末尾坐标为n-1的是完全二叉树。此法适用于节点类，方便加字段才行。但是第二种方法万能。
层序遍历时，碰到某个节点的孩子有空时，如len(queue)+len(has_output)<n的，说明空比节点先出现，不是CBT。直接退出
'''
from collections import deque
n = int(input())
nodeset = set(range(n))
l = [None]*n
for i in range(n):
    a,b = input().split()
    a = None if a=='-' else int(a)
    b = None if b=='-' else int(b)
    l[i] = [a,b]
    nodeset.discard(a)
    nodeset.discard(b)

root = nodeset.pop()
q = deque([root])
hasoutput = []
flag = 'YES'
while flag=='YES' and len(q)>0:
    p = q.popleft()
    hasoutput.append(p)
    if l[p] is None:
        continue
    for son in l[p]:
        if son is None and len(hasoutput)+len(q) < n:
            flag= 'NO'
            break
        elif son is not None:
            q.append(son)


if flag == 'YES':
    print(flag,hasoutput[-1])
else:
    print(flag, root)
