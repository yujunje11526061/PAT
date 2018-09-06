#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
注意每次转向需要更新的坐标以及每次启动前检查是否满足cnt<N，以应对只有一列的情况
主要难点在于数组越界。
'''
from math import sqrt, ceil

N = int(input())

m = ceil(sqrt(N))
while m <= N and N % m > 0:
    m += 1

n = N//m

# print(m,n)
seq = sorted(map(int, input().split()), reverse=True)
mat = [[None]*n for i in range(m)]
cnt = 0
i,j = 0,0
left = 0
right = n-1
up = 1
down = m-1
while cnt<N:
    while j<=right:
        mat[i][j] = seq[cnt]
        cnt += 1
        j += 1
    j -= 1
    i += 1
    right -= 1
    while cnt<N and i<=down:
        mat[i][j] = seq[cnt]
        cnt += 1
        i +=1
    i -= 1
    j -=1
    down -= 1
    while cnt< N and j>=left:
        mat[i][j] = seq[cnt]
        cnt += 1
        j -= 1
    j +=1
    i -= 1
    left += 1
    while cnt< N and i>=up:
        mat[i][j] = seq[cnt]
        cnt += 1
        i -=1
    i += 1
    j += 1
    up += 1

for line in mat:
    print(*line)
