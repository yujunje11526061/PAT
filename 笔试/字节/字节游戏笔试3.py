#!/usr/bin/env python
# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    MAX = 9999999999
    N, P = map(int, input().strip().split())
    table = list(map(int, input().strip().split()))
    dp = [MAX] * N

    for i in range(N - 1, -1, -1):
        if table[i] == 0:
            dp[i] = MAX
        elif table[i] >= N - i:
            dp[i] = 1
        else:
            left = min(i + 1, N - 1)
            right = min(i + table[i], N - 1)
            x = min(dp[left:right + 1])
            dp[i] = MAX if x == MAX else x + 1

    for i in range(N):
        if(table[i]==0):
            continue
        left = max(0, i - table[i])
        right = max(0, i - 1)
        y = min(dp[left: right + 1])
        if y == MAX:
            continue
        else:
            dp[i] = min(dp[i], y + 1)

    if dp[P - 1] == MAX:
        print(-1)
    else:
        print(dp[P - 1])

# main()

while 1:
    try:
        main()
    except:
        break
