#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
LIS
将原问题抽象成求最长递增子序列的问题（LIS），当然这里可以相等，是求最长非减子序列
对于序列中任一位置i，记到该位置位置，已知LIS的大小为dp[i].
遍历其前面的位置，若某一位置j的值不大于i的值，则长度为max(dp[i], dp[j]+1)
在遍历过程中不断刷新dp[i]，然后每轮i结束去和已得出的maxn比，取大的长度
复杂度O(n^2)

二分法优化LIS：
效率提升巨大，O(nlogn)
二分查找标准型（应熟记）：
循环条件应该为while start <= end，mid = (start+end)//2， 变更范围的操作为mid-1，mid+1
因查找不到而跳出循环时，必定满足 l[end] < item < l[start], 且数组下标 end + 1 = start
且循环自然自然中止时，初始start <= 最终end < 最终start <= 初始end，端点指针不会越界

LCS (https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)
原始LCS问题的一个计算最长公共子序列的方法如下，以两个序列 X、Y 为例子：
设有二维数组 f[i][j] 表示 X 的 i 位和 Y 的 j 位之前的最长公共子序列的长度，则有：
f[1][1] = same(1,1)
f[i][j] = max(f[i-1][j-1] + same(i,j),f[i-1][j],f[i][j-1]})
其中，same(a,b)当 X 的第 a 位与 Y 的第 b 位完全相同时为“1”，否则为“0”。
此时，f[i][j]中最大的数便是 X 和 Y 的最长公共子序列的长度，依据该数组回溯，便可找出最长公共子序列。
用(len(X)+1)*(len(Y)+1)的二维表辅助求解，第一行第一列全为0
该算法的空间、时间复杂度均为O(mn)，经过优化后，空间复杂度可为O(n)，时间复杂度为O(nlogn)。
'''
# ===============================================================================
# LIS写法
# 把数字的先后顺序转换为id，id越小，顺序越靠前。不要和数字本身的大小混淆
# 考试的时候用字典更好写。不用担心越界和下标。但由于总长确定，数组更快更省空间

# N = int(input())
# l0 = list(map(int, input().split()))
# l1 = list(map(int, input().split()))
# id = 0
# d = [None] * (201)
# for i in l0[1:]:
#     d[i] = id
#     id += 1
#
# l = [d[i] for i in l1[1:] if d[i] is not None]
# dp = [1] * len(l)
# maxn = 0
# for i in range(len(l)):
#     for j in range(i):
#         if l[j] <= l[i]: # 此题包括等于的
#             dp[i] = max(dp[j] + 1, dp[i])
#     maxn = max(dp[i], maxn)
#
# print(maxn)
# ------------------------------------------------------------------------------
# LIS +二分法改进 （此题包括等于的）
# 维护一个数组tail[]记录对应长度的IS的最小末尾数字是啥
# tail[i] = num, 表示，长度为i的IS，最小末尾数字为num
N = int(input())
l0 = list(map(int, input().split()))
l1 = list(map(int, input().split()))
id = 0
d = [None] * (201)
for i in l0[1:]:
    d[i] = id
    id += 1

def find_position_and_change(s,e,item):
    if i >= tail[e]: # 因为此题可以重复
        tail.append(item)
        return
    if i<tail[s]:
        tail[s] = item
        return
    while s<=e:
        mid = (s + e) // 2
        if tail[mid] == item: # 因为此题可以重复
            tail[mid+1] = item
            return
        elif tail[mid] < item:
            s = mid+1
        else:
            e = mid-1
    tail[s] = item


l = [d[i] for i in l1[1:] if d[i] is not None]
tail = [None, l[0]]
for i in l[1:]:
    find_position_and_change(1,len(tail)-1, i)

print(len(tail)-1)


# ===============================================================================
# LCS写法 （变种之允许重复）
# 用的是值匹配，探索过程中已经隐含了顺序规则，故不用显示地用id大小表示顺序，只需用一个集合去除不要的数字
#
# N = int(input())
# l0 = list(map(int, input().split()))
# l1 = list(map(int, input().split()))
#
# l0, l1 = l0[1:], l1[1:]
# SS = set(l0)
# X = [None] + l0
# Y = [None] + [i for i in l1 if i in SS]
# x, y = len(X), len(Y)
# maxn = 0
# l = [[0] * y for i in range(x)]  # x行 * y列
# for i in range(1, x):
#     for j in range(1, y):
#         # 区别于原始LCS，此题因为可以重复，所以l[i-1][j]和l[i][j-i]都要+(X[i] == Y[j])
#         l[i][j] = max(l[i - 1][j - 1] + (X[i] == Y[j]), \
#                       l[i - 1][j] + (X[i] == Y[j]), \
#                       l[i][j - 1] + (X[i] == Y[j]))
#     maxn = max(maxn, l[i][j])
#
# print(maxn)
