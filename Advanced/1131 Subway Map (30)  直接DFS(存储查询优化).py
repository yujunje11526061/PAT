#!/usr/bin/env python
# -*- coding:utf-8 -*-
N = int(input())

tbl = [[] for i in range(10000)]
# linemap = [[for j in range(10000)] for i in range(10000)]  二维数组内存开销太大。
# 优化一, 散列表. 点稀疏时用较好.
# linemap = {}
# linemap[(x,y)] = lineNum  C++可以根据编号特征用10000*x+y来作为键,这样键不会重复.
# 优化二,化为一维数组. 点很密时较好.
# linemap = [for i in range(100000000)]
# linemap[x*10000+y] = line

# 本题点很稀疏,远达不到四位数,故用散列表.
linemap = {}

for i in range(1, N + 1):
    line = map(int, input().split())
    next(line)
    prestation = next(line)
    for cntstation in line:
        tbl[prestation].append(cntstation)
        tbl[cntstation].append(prestation)
        linemap[prestation * 10000 + cntstation] = linemap[cntstation * 10000 + prestation] = i
        prestation = cntstation


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


def DFS(node, temppath, stNum):
    global finalTransferNum,finalStaNum,finalPath
    # 到达此node的信息在前一层都已经算清,此时判断该节点是就此终结还是继续扩展
    if node == end:
        # 因为线路不多,到达目的地计算转乘次数比每次中间都算转乘次数要省时间,且把算判断转乘放在if语句最后面判断,即便此处到达目的地都要算两次.
        if stNum < finalStaNum or (stNum == finalStaNum and transfer(temppath) < finalTransferNum):
            finalPath = list(temppath)
            finalTransferNum = transfer(temppath)
            finalStaNum = stNum
        return
    else:
        for j in tbl[node]:
            if visited[j] == 1: continue
            # 得到一个新的活结点,下一轮DFS开始时应把记录同步更新到下一个活结点
            visited[j] = 1
            temppath.append(j)
            DFS(j, temppath, stNum + 1)
            # 回溯过程, 探索返回时,恢复到本函数栈帧原先的样子. 某些情况, 此时可以加剪枝条件来根据已有信息加速后续探索
            # 如果不恢复,单纯把信息当成参数不断传进去,在新的栈帧再建拷贝,则会在空间上和时间上带来很多不必要的拷贝开销.
            visited[j] = 0
            temppath.pop()


K = int(input())
for k in range(K):
    start, end = map(int, input().split())
    finalPath = []
    finalTransferNum = 9999
    finalStaNum = 9999
    temppath = [start]
    visited = [0] * 10000
    visited[start] = 1
    DFS(start, temppath, 0)
    print(len(finalPath) - 1)
    transfer(finalPath,True)
