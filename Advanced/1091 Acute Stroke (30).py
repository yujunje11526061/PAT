#!/usr/bin/env.python
# -*- coding:utf-8 -*-
M, N, L, T = map(int, input().split())


def get_around(p):
    x, y, z = p
    return [(x, y, z + 1), (x, y, z - 1), \
            (x, y - 1, z), (x, y + 1, z), \
            (x - 1, y, z), (x + 1, y, z)]


tot = 0
matrix = [[[0] * L for _ in range(N)] for i in range(M)]  # 三维空间
visited = [[[0] * L for _ in range(N)] for i in range(M)]
# s = set()  # 记录所有为1的点的元祖坐标
# 用集合内存爆了
# 用数组时间爆了
s = []
for z in range(L):
    for x in range(M):
        row = map(int, input().split())
        y = 0
        for value in row:
            if value:
                s.append((x, y, z))
                matrix[x][y][z] = 1
            y += 1

while len(s) > 0:
    start = s.pop()
    x, y, z = start
    if visited[x][y][z] == 1:
        continue
    count = 0
    visited[x][y][z] = 1
    stack = [start]
    while len(stack) > 0:
        now = stack.pop()
        count += 1
        around = get_around(now)
        for point in around:
            i, j, k = point
            if i < 0 or j < 0 or i > M - 1 or j > N - 1 or k < 0 or k > L - 1 \
                    or matrix[i][j][k] == 0 or visited[i][j][k] == 1:
                continue
            visited[i][j][k] = 1
            s.remove(point)
            stack.append((i, j, k))
    tot += count if count >= T else 0

print(tot)
