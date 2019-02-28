#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
f(i) =  f(i-1)+l[i]   or  l[i] 对应curSum
maxSum = max(历史curSum)
'''

K = int(input())
l = list(map(int, input().split()))

maxSum = -8888888888
curSum = 0
isAllNegetive = True
p,q = 0, K-1
for i in range(K):
    if l[i]>=0:
        isAllNegetive = False
    if curSum<0 or (maxSum == -8888888888 and curSum==0): # 前面的为负，则不要，curSum为当前位置值, 后半个条件是保证前面全负碰到0时有下标记录
        curSum = l[i]
        pc,qc = i,i
    elif curSum==0 and maxSum!=-8888888888:
        curSum = l[i]
        qc = i
    else:
        curSum += l[i]
        qc += 1

    if curSum>maxSum:
        maxSum = curSum
        p,q = pc,qc
    elif curSum==maxSum and (pc,qc)<(p,q):
        p,q =pc,qc


if isAllNegetive:
    maxSum=0
    p,q = 0,K-1

print(maxSum,l[p],l[q])