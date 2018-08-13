N, M, start, end = map(int, input().split())
nt = list(map(int, input().split()))
inf = float('inf')

# matrix = [[inf]*N for i in range(N)]
# print(matrix)
table = [[] for i in range(N)]
for _ in range(M):
    i, j, w = map(int, input().split())
    table[i].append((w, i, j))
    table[j].append((w, j, i))

# print(table)    优化了数据的读取
# print(matrix)
# table = []
# for i in range(N):
#    table.append([(matrix[i][j], i, j) for j in range(N) if matrix[i][j] != inf])
# print(table)

visited = [0] * N  # 标记该点有没有被收录
path = [None] * N  # 记录从start到某点最短路径的前一个途经点
dist = [inf] * N  # 存储各个点到start的临时最短路径
nsr = [0] * N  # 从start到某点的最短路径数目
hands = [0] * N  # 从start到某点的各最短路径上可以征集的最大人手

dist[start] = 0
nsr[start] = 1
hands[start] = nt[start]

# def find_min_dist_by_list(dist):
#     i = None
#     d = inf
#     for v in range(N):
#         if not visited[v] and dist[v] < d:
#             i = v
#             d = dist[v]
#     return i  # 返回未收录的临时最短路径最小的点,不存在则为None


# def siftup(heap, e):
#     heap.append(None)
#     i = len(heap)-1
#     j = (i-1)//2
#     while j>=0:
#         if heap[j] > e:
#             heap[i] = heap[j]
#             i = j
#             j = (i-1)//2
#         else:
#             break
#     heap[i] = e
#
#
# def siftdown(heap):
#     e = heap.pop()
#     start = 0
#     end = len(heap)-1
#     i = start
#     j = 2*i+1
#     while j < end:
#         if j+1 <= end and heap[j] > heap[j+1]:
#             j += 1
#         if heap[j] < e:
#             heap[i] = heap[j]
#             i = j
#             j = 2*i+1
#         else:
#             break
#     heap[i] = e
#
#
# # def find_min_dist_by_heap(heap):
# #     if len(heap) == 0:
# #         return None
# #     elif len(heap) == 1:
# #         return heap.pop()[1]
# #     else:
# #         i = heap[0][1]
# #         siftdown(heap)
# #         return i
# #
# # heap = [(dist[start], start)]

import heapq  # 用标准库里的优先队列模块heapq

heap = [(dist[start], start)]

while 1:
    # 找到未收录的临时最短路径最小的点
    # 可以遍历所有点，也可以把可触及的邻接点的信息另外放进一个最小堆，不能在原dist上直接调整成堆，不然按索引改dist中元素会错乱
    # 每更新一个dist元素把对应信息放进堆里，即使原来堆里已有到某点的距离信息，堆也会把更新后的更短的距离自动调整到上层
    # 堆中原有的那些未更新距离的条目后面会被visited过滤掉
    # 建堆操作比较复杂，本题时间已经足够
    # i = find_min_dist_by_list(dist)
    # 用最小堆优化了未收录最近点的取法。
    # i = find_min_dist_by_heap(heap)
    # 已经没有可收录的点,跳出循环
    # if i == None:
    #     break
    # 处理早先进入堆的点的距离信息，因为后来更新后距离更短，那个条目先出来了，所以老的没用了
    # 但是老的也可能被弹出来，此时不能break，应continue，因为可能有别的未收录的但是距离比该点老记录还大的

    if len(heap) == 0:
        break
    else:
        i = heapq.heappop(heap)[1]
    if visited[i]:
        continue

    visited[i] = 1

    # 考察收录i后对i未收录的邻接点j的dist的影响
    # 已收录的j的最短路径必定是定下来的,否则i为j的前驱点，i不可能比j后收录
    for w, i, j in table[i]:
        if not visited[j]:
            if dist[i] + w < dist[j]:
                dist[j] = dist[i] + w
                nsr[j] = nsr[i]
                hands[j] = hands[i] + nt[j]
                path[j] = i
                # siftup(heap, (dist[j], j)) #把更新后的更短的路径信息放入堆中
                heapq.heappush(heap, (dist[j], j))
            elif dist[i] + w == dist[j]:
                nsr[j] += nsr[i]
                if hands[i] + nt[j] > hands[j]:
                    hands[j] = hands[i] + nt[j]
                    path[j] = i  # 记录路径最短前提下人手最多的路径

print(nsr[end], hands[end])
# print(nsr)
# print(hands)


