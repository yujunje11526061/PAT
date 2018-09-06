#!/usr/bin/env.python
# -*- coding:utf-8 -*-
from collections import defaultdict, deque

n, m= map(int ,input().split())
table = [None for i in range(n+1)]
for i in range(m):
    id, num, *son = map(int, input().split())
    table[id] = son

level = 1
d = defaultdict(lambda :0)
q = deque([[1, 1]])
while len(q)>0:
    i, level = q.popleft()
    d[level] +=1
    try: # 只有一个结点的情况下，不加try会报错
        for j in table[i]:
            if table[j] is not None: # 末端叶节点就索性不入队了，少一轮出入操作
                q.append([j, level+1])
            else:
                d[level+1] += 1
    except:
        continue
maxlevel = max(d, key= lambda x: d[x])
count = d[maxlevel]
print(count, maxlevel)
