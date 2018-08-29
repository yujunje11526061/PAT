#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, M, S = map(int, input().split())
w = list(map(int, input().split()))

graph = [None for i in range(N)]
for i in range(M):
    id, num, *children = map(int, input().split())
    graph[id] = children

path_weight = [None for i in range(N)]
weight = [0]*N
def dfs(root):
    global path_weight, weight
    leafs = []
    weight[root] = w[root]
    path_weight[root] = [w[root]]
    stack = [root]
    while len(stack) > 0:
        p = stack.pop()
        if graph[p] is not None:
            for child in graph[p]:
                weight[child] = weight[p]+w[child]
                path_weight[child] = path_weight[p]+[w[child]]
                stack.append(child)
        else:
            leafs.append(p)
    return leafs


if N==1 and w[0] == S:
    print(S)
else:
    leafs = dfs(0)
    ll = []
    for leaf in leafs:
        if weight[leaf] ==S:
            ll.append(path_weight[leaf])
    ll.sort(reverse=True)
    for path in ll:
        print(*path)