#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
本题关键在于PeekMedian操作，若每次都对堆栈的镜像进行排序，则必定超时。
故用树状数组来加速查询。
树状数组最初时为了解决这么一个问题，有一个数组，对每个位置，想获得其累计和。
若数组存原始数字，则查询(求和)需要O(n)时间复杂度，更新需要O(1)
若每个位置存累计和，则可以以O(1)获得每个位置的值(减去前一位的)和累计和，但是若有数据更新，则后面的都要更新，为O(n)
树状数组是为了兼顾两种操作，使得时间复杂度都为O(log n)
将原始数组从1号位开始划分，每一段都为2格。如图 'https://blog.csdn.net/jiayizhenzhenyijia/article/details/80066292'
用另一个数组c记录区间累计和。区间的的划分可由二进制数的操作相关来规定。

对于x的二进制表示，如x = 010111000，需要得到最低位1所表示的数，即1000。
计算机中负数是通过补码来表示的。负数的补码=反码+1，负数的反码为符号为不变，后面依次取反
010111000对应的负数原码为110111000，其补码 = 101000111+1 = 101001000，x&(-x)，按位与，都为1才是1，可以得到1000
此种取最末尾1开始的串的操作通常定义为函数lowbit(x)。则对任意二进制数，可以通过lowbit(x)拆分成多个开头为1后面全0的小串相加
如 1111 = 1000 + 100 + 10 + 1。这些小串对应的十进制数正好是2的等比数列。以此数列为区间端点，正好对应了树状数组中每一个大区间。
去尾：1111 去尾得 1110 去尾得1100，即x -= lowbit(X)
对应到树状数组：
可以看出 c(8) = c[4]+c[6]+c[7]+a[8], c[7] = a[7]....
若要统计前8个的总和，则直接从数组c中获得c[8]，若要获得前7个的则，则从数组c中获得c[7]+c[6]+c[4]
8的二进制为1000，去尾为0，故可以直接得到getsum(8) = c[8]
7的二进制为111，连续去尾得到非零序列，110，10，对应十进制数6，4，而getsum(7) = c[7]+c[6]+c[4]
可以发现，想要得到前i个数的和，只需对下标i的二进制数不断去尾，从树状数组C中取小区间和累加即可
从而把求和过程与去尾过程相关联。
若要更新，则只要把树状数组里路径上的点更新即可。如a[3]发生改动，则c[3],c[4],c[8],c[16]...一系列都要改动。那么这些下标有啥规律呢。
3：11，4：100，8：1000，16：10000，可以看到为前面增加一位1，后面全变成0，即地推规律为下标x += lowvit(x)
从后去尾和从前更新的时间复杂度都为O(log n)，分别对应查询累计和和更新树状数组的操作。

本题中的累计和代表数值不超过下标i的key个数，这些key最大就是i。从而要求第k个小的值，只需求出累计和为k的最小的下标即可
为什么是最小下标。比如插入一个5，则getsum(i)只要i>=5都为1，只有取最小下标，才能使得下标==key，从而输出下标即可表示那个key
进栈和出栈都要进行，后推更新
查询时则可以通过二分法缩小下标范围，找到使得getsum(i)==k 的最小i即可。
'''
import math

N = int(input())
stack = []
maxn = 100001
c = [0] * maxn


def lowbit(x):
    return x & (-x)


def update(i, num):
    while i < maxn:
        c[i] += num
        i += lowbit(i)

def getsum(i):
    sum_ = 0
    while i >= 1:
        sum_ += c[i]
        i -= lowbit(i)
    return sum_

def PeekMedian(k):
    s, e = 1, maxn
    while s < e:
        mid = (s + e) // 2
        count = getsum(mid)
        if count >= k: # 可能有好多个i，对应getsum(i)==k的，按题意应要找到最小的
            e = mid
        else:
            s = mid + 1
    return s

for i in range(N):
    cc = input()
    if cc[1] == 'u':
        temp = int(cc.split()[1])
        stack.append(temp)
        update(temp, 1)
    elif cc[1] == 'o':
        if len(stack) > 0:
            temp = stack.pop()
            update(temp,-1)
            print(temp)
        else:
            print('Invalid')
    else:
        if len(stack) > 0:
            k = math.ceil(len(stack) / 2)
            print(PeekMedian(k))
        else:
            print('Invalid')
