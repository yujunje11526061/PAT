#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
Dijkstra 最短路径算法. 需要记录路径, 沿途需要操作, 更新需要携带的车的数量. 主权是最短路, 第二权是带出量, 第三权是带回量
比如一条路上bike数为 3 10，是send2，back5，而不是back3。
次数不能只用Dijkstra算法, 因为不是一路进,也不是一路出,路上有进有出,相当于有负权的情况. Dijkstra和DFS结合
题目示例中的&gt有问题,应该是->

Dijkstra() {
  初始化;
  for(循环n次) {
    u = 使dis[u]最小的还未被访问的顶点的编号;
    记u为确定值;
    for(从出发能到达的所有顶点v){
      for(v未被访问 && 以u为中介点使s到顶点v的最短距离更优)
        优化dis[v];
    }
  }
}
'''
import heapq

C, N, p, M = map(int, input().split())

capacity = map(int, input().split())
diff = [0] + [int(i - C/2) for i in capacity]

table = [[] for i in range(N + 1)]
for _ in range(M):
    i, j, w = map(int, input().split())
    table[i].append([w, j])
    table[j].append([w, i])

# Dijkstra算法找出最短路的大小
inf = float('inf')
visited = [0] * (N + 1)
path = [[] for i in range(N + 1)]
dist = [inf] * (N + 1)
dist[0] = 0
h = [(dist[0], 0)]
# Dijkstra算法找到所有最短路径
while len(h)>0:
    _, i = heapq.heappop(h)  # 未收录的最近的点
    if visited[i] == 1:
        continue
    if i == p: # 找到目标结点,直接跳出
        break
    visited[i] = 1
    # 更新i的邻接点
    for w, j in table[i]:
        if visited[j]:
            continue
        if dist[j] >= dist[i] + w:
            if dist[j] > dist[i] + w:
                dist[j] = dist[i] + w
                path[j] = [i]
                heapq.heappush(h, (dist[j], j))
            else:
                path[j].append(i)  # 搜集所有最短路径

# path代表的二维数组是一个由起点与终点的间所有最短路径构成的图,他是原图的子图, 且可以看成是一个反向有向图,因为记录的是前驱结点的编号
# 以第二权和第三权来考察这些最短路径
# 重新建图, 正向思考比回溯思考来得容易
t2 = [[] for i in range(N + 1)]
for i in range(N+1):
    for j in path[i]: # j是i的前驱结点
        t2[j].append(i)

Need = inf
Back = inf
need, back = 0, 0
R = None
def dfs(s, need, back, road:list):
    global Need, Back, R
    if s == p:  # 因为t2中包含了一些无关的点的路径,故一定是走到目标点p才算.别的无关路径会在函数中自然走到头.
        if need<Need:
            Need = need
            Back = back
            R = road
        if need == Need:
            if back < Back:
                Back = back
                R = road
        return
    for e in t2[s]:
        r = list(road)
        need2, back2 = need, back
        if diff[e] < 0:
            if back2 + diff[e] >= 0:
                back2 += diff[e]
            else:
                need2 = -(back2+diff[e])+need2
                back2 = 0
        if diff[e] > 0:
            back2 += diff[e]
        r.append(e)
        dfs(e, need2, back2, r)

dfs(0, need, back, [0])

num = len(R) - 1
road = '0' + '->{}' * num

print(Need, road.format(*R[1:]), Back)
