#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
思路：
对于一个树状图（边数 = 顶点数 - 1
的连通图，下限的边数，连通则必无环），最大距离一定产生于端点之间，这些点可能不止一个，记为集合U
对任意一个节点A做DFS，得到最远的点集S，对S中任一端点B，B一定属于U，集S为U的子集
---------------------------------------------------------------------------
证明：反证法
若B不属于U，则存在属于U的两个端点C，D，使得CD距离最大
由A的DFS可知，AB > AC, AB > AD

if A在CD路径上:
    则C，D不可能都在AB路径上，否则CD < AB，与CD距离最大的假设矛盾
    if C 在AB路径上:
        则CD = AC + AD < AB + AD = BD，即CD < BD，与CD距离最大的假设矛盾
    if D 在路径AB上:
        同上
    if C，D都不在路径AB上:
        CD = AC + AD < AB + AD = BD
        CD = AC + AD < AC + AB = CB非常
        与CD距离最大的假设矛盾
else:
    根据树状图的定义，连通且无环，则在路径CD上，有且仅有一个点F，构成路径AF
    此时，不论F在不在AB上，由A的DFS，都容易证明BF > CF, BF > DF
    此时把F当成是A的角色，上一个分支已经讨论过此问题。仍旧与CD距离最大的假设矛盾

从而假设不成立，B必为U的一员，S为U的子集
---------------------------------------------------------------------------
最大距离产生在B和别的端点之间。此时对B做DFS，便可以得到与B最远的端点集H
从而得到U = union(S, H)
故本题思路为两轮DFS。中间顺带记录深度和判断是否连通图。BFS同理也能做。
'''
n = int(input())
table = [[] for i in range(n + 1)]
for i in range(n - 1):
    i, j = map(int, input().split())
    table[i].append(j)
    table[j].append(i)

s0 = set(range(1, n + 1))

# 第一轮dfs
count = 0

while len(s0) > 0:
    s = set()
    count += 1
    x = s0.pop()
    stack = [x]
    MAX = 0
    depth = [0] * (n + 1)
    ss = {x}
    while len(stack) > 0:
        i = stack.pop()
        s.add(i)
        for j in table[i]:
            if j in s0:
                s0.remove(j)
                stack.append(j)
                depth[j] = depth[i] + 1
                if depth[j] >= MAX:
                    if depth[j] > MAX:
                        MAX = depth[j]
                        ss.clear()
                    ss.add(j)

if count > 1:
    print('Error: {} components'.format(count))

else:
    MAX = 0
    depth = [0] * (n + 1)
    x = ss.pop()
    ss.add(x)
    stack = [x]
    ss2 = {x}
    s0 = set(range(1, n + 1))
    while len(stack) > 0:
        i = stack.pop()
        for j in table[i]:
            if j in s0:
                s0.remove(j)
                stack.append(j)
                depth[j] = depth[i] + 1
                if depth[j] >= MAX:
                    if depth[j] > MAX:
                        MAX = depth[j]
                        ss2.clear()
                    ss2.add(j)

    ss3 = ss.union(ss2)
    ss4 = sorted(ss3)
    for i in ss4:
        print(i)
