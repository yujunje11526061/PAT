#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
简单模拟加动态规划严重超时
考虑到都是正整数，到0点的距离时递增的，可以用二分法
S[i]表示0点到i点的累积和。从而S[j]-S[i]+l[i]即为i-j的和
'''

N, M = map(int, input().split())
l = list(map(int, input().split()))

s = [0] * N
s[0] = l[0]
e = 1
while e < N:
    s[e] = s[e - 1] + l[e]
    e += 1
# print(s)

def cal(i, j):
    global xm, p, q
    ss = s[j] - s[i] + l[i]
    if ss == M:
        print('{}-{}'.format(i + 1, j + 1))
        return 1
    elif ss < M:
        return 0
    else:
        head, tail = i, j
        while head <= j and tail >= i and head <= tail:
            mid = (head + tail) // 2
            x = s[mid] - s[i] + l[i]
            if x == M:
                print('{}-{}'.format(i + 1, mid + 1))
                return 1
            elif x > M:
                tail = mid - 1
                if flag == 0:
                    if x < xm:
                        xm = x
                        p, q = [i], [mid]
                    elif x == xm:
                        p.append(i)
                        q.append(mid)
            else:
                head = mid + 1
        return 0


xm = float('inf')
p, q = [], []
flag = 0
for i in range(N):
    flag = cal(i, N - 1) if flag == 0 else flag+cal(i, N-1)

if flag == 0:
    for a, b in zip(p, q):
        print('{}-{}'.format(a + 1, b + 1))
