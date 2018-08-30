#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
动态规划法，将币种按面值排序。从小面值开始拿，算到背包容量为M为止。
虽然是多重背包问题，但是同样的币种可以看成各种独立的，还是有限个，可以按01背包来进行动态规划
这里的规划表dp[i][j]记录的是用币序列前（i+1）个币中取，凑成总权值M所对应的最小序列。
这个表的价值更新与否（序列的大小比较）是通过把解序列中的币值用列表存储来进行比较的。
由于表的价值计算过程中涉及到列表相加与比较，以及两层循环，故总的时间复杂度反而较高。而且也不能统计数目即输出全部可能。
'''
N, M = map(int, input().split())
l = sorted(map(int, input().split()))  # 有序的排列即代表了权重的数组
inf = float('inf')
dp = [[[0]] + [[inf]] * M for i in range(N)]


def knap():
    for i in range(N):
        if l[i] > M:
            return
        for j in range(M+1):
            if l[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j - l[i]] + [l[i]], dp[i - 1][j])


knap()
minseq = [inf]
for i in range(N):
    if dp[i][M] < minseq:
        minseq = dp[i][M]
if minseq[0] == inf:
    print('No Solution')
else:
    print(*minseq[1:])
