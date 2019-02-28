#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
直接dfs，当存在环时非常麻烦，找到最短路过程中，环中有些部分相当于经过了了很多次。非常耗时。
得把visited，path等很多参数反复传参并新建副本，耗时耗内存。递归程序也不好调试。
应该先按各权值均为1的最短路径问题，用Dijkstra算法初筛一次，记录最短路径，然后回溯。
回溯过程相当于一个有向图，无环，计算量一下子小很多。
最好先Dijkstra， 但由于中间站点不唯一，故统计所有等长路径后得再DFS。深搜回溯(要恢复信息)的思想.
'''
import heapq as hq

N = int(input())
table = [[] for i in range(10000)]
linemap = {}
for line in range(1, N + 1):
    n, *sta = map(int, input().split())
    for i in range(n - 1):
        table[sta[i]].append(sta[i + 1])
        table[sta[i + 1]].append(sta[i])
        linemap[sta[i+1]*10000+sta[i]]=linemap[sta[i]*10000+sta[i+1]]=line

def Dijkstra(s, e):
    visited = [0] * 10000
    inf = float('inf')
    path = [[] for i in range(10000)]
    dist = [inf] * 10000
    dist[s] = 0
    h = [[dist[s], s]]  # 距离起点的距离， i的编号
    while len(h) > 0:
        _, i = hq.heappop(h)
        if visited[i]:
            continue
        if i == e:
            return path
        visited[i] = 1
        for j in table[i]:
            if visited[j]:
                continue
            if dist[j] > dist[i] + 1:
                dist[j] = dist[i] + 1
                path[j] = [i]
                hq.heappush(h, [dist[j], j])
            elif dist[j] == dist[i] + 1:
                path[j].append(i)
    return path

def transfer(thispath, forOutPut=False):
    transferNum = 0
    preLine = 0
    prestation = pretransfer = thispath[0]
    for cntstation in thispath[1:]:
        if linemap[prestation * 10000 + cntstation] != preLine:
            if forOutPut is True and preLine != 0:
                print("Take Line#{} from {:0>4} to {:0>4}.".format(preLine,pretransfer, prestation))
            transferNum += 1
            pretransfer = prestation
            preLine = linemap[prestation * 10000 + cntstation]
        prestation = cntstation
    if forOutPut is True and prestation == end:
        print("Take Line#{} from {:0>4} to {:0>4}.".format(preLine, pretransfer, prestation))
    return transferNum


def DFS(node, temppath):
    global finalTransferNum,finalPath
    # 到达此node的信息在前一层都已经算清,此时判断该节点是就此终结还是继续扩展
    if node == start:
        thistransferNum = transfer(temppath)
        if thistransferNum < finalTransferNum:
            finalPath = list(temppath)
            finalTransferNum = thistransferNum
        return
    else:
        for j in path[node]:
            if visited[j] == 1: continue
            # 得到一个新的活结点,下一轮DFS开始时应把记录同步更新到下一个活结点
            visited[j] = 1
            temppath.append(j)
            DFS(j, temppath)
            # 回溯过程, 探索返回时,恢复到本函数栈帧原先的样子. 某些情况, 此时可以加剪枝条件来根据已有信息加速后续探索
            # 如果不恢复,单纯把信息当成参数不断传进去,在新的栈帧再建拷贝,则会在空间上和时间上带来很多不必要的拷贝开销.
            visited[j] = 0
            temppath.pop()


qn = int(input())
for _ in range(qn):
    start, end = map(int, input().split())
    path = Dijkstra(start, end)
    finalPath = []
    finalTransferNum = 9999
    temppath = [end]
    visited = [0] * 10000
    visited[end] = 1
    DFS(end, temppath)
    finalPath.reverse()
    print(len(finalPath)-1)
    transfer(finalPath,forOutPut=True)
