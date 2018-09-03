#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
BFS
一个课程的人肯定属于一个团体，一个人选了多门课相当于连接了多个团体
故把课程看成顶点，通过桥梁人来遍历，求出有几个连通的课程集，连通课程里的人并起来就是人的团体
直接用字典存储每个课和上这个课的人的集合。BFS遍历的是课程，遍历途中把上课程的人并起来。并从总课程集合里去除。
然后从上课的人出去找新的课程入队
!!! a.update(b) 是把新的并集赋值给a，a.union(b)是返回一个新的并集
'''
from collections import defaultdict, deque
N = int(input())
totcourse = set()
course = defaultdict(set)
id = defaultdict(list)
for i in range(N):
    s = map(int, input().split()[1:])
    for j in s:
        course[j].add(i)
        id[i].append(j)
        totcourse.add(j)

record = []
visited = defaultdict(lambda :0)
while len(totcourse)>0: # 从总课程里找连通课程的个数
    p = totcourse.pop()
    cluster = set(course[p])
    visited[p] = 1
    queue = deque([p])
    while len(queue)>0:
        c = queue.popleft()
        for stu in course[c]:
            for nc in id[stu]:
                if not visited[nc]:
                    visited[nc] = 1
                    cluster.update(course[nc])  # !!! a.update(b) 是把新的并集赋值给a，a.union(b)是返回一个新的并集
                    totcourse.remove(nc)
                    queue.append(nc)
    record.append(len(cluster))

record.sort(reverse=True)
print(len(record))
print(*record)




