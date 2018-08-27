#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
简单模拟加动态规划严重超时
考虑到都是正整数，到0点的距离时递增的，可以用二分法
S[i]表示0点到i点的累积和。从而S[j]-S[i]+l[i]即为i-j的和
'''

N, M = map(int, input().split())
l = list(map(int, input().split()))

ml = float('inf')
p, q = [], []
flag = 0
flag2 = 0
i = 0
while i< N:
    if flag2 == 0:
        j = i
        total = l[i]
    flag2 = 0
    while j < N:
        if i == j:
            if l[i] == M:
                flag = 1
                print('{}-{}'.format(i+1, j+1))
                break
            elif flag == 1 and l[i] > M:
                break
            elif flag ==0:
                if l[i] > ml:
                    break
                elif i == j and M < l[i] < ml:
                    ml = l[i]
                    p = [i]
                    q = [j]
                    break
                elif i == j and M<l[i] == ml:
                    p.append(i)
                    q.append(j)
                    break
        elif i < j:
            total += l[j]
            if total == M:
                flag = 1
                flag2 = 1
                print('{}-{}'.format(i+1, j+1))
                j += 1
                total = total - l[i]
                break
            elif flag==1 and total > M:
                flag2 = 1
                total = total - l[i]-l[j]
                break
            elif flag == 0:
                if total > ml:
                    break
                elif M < total < ml:
                    ml = total
                    p = [i]
                    q = [j]
                    break
                elif M < total == ml:
                    p.append(i)
                    q.append(j)
                    break

        j += 1
    i += 1

if flag == 0:
    for i,j in zip(p,q):
        print('{}-{}'.format(i+1, j+1))


