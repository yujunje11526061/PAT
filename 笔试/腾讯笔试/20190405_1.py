#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
100 6
1
5
8
20
22
43
答案10
首先1要选，问题是选几个
找到下一个硬币，5，那么1要选4个，少了不行，多了没用
然后开始考虑5，1已经有4个了，也就是1-4全有了，如果有x个5，那么1到5x+4也全有了
5后面的是8，所以x=1就行了，5x+4=9，也就是1到9数字全有了
然后考虑8选几个，首先前面的和是4*1+1*5=9，如果选x个8，那么1到8x+9的数字全有了，8后面的是20，所以x=2，8x+9=25
依此类推
'''
from math import ceil

m, n = map(int, input().split())
l = []
for i in range(n):
    s = int(input())
    l.append(s)

l.sort()

if len(l) == 0 or l[0] > 1:
    print(-1)
elif n == 1 and l[0] == 1:
    print(m)
else:
    cnt = [l[1] - 1]
    cover = l[1] - 1
    prev = l[1]

    for v in l[2:]:
        cntPrev = int(ceil((v - 1 - cover) / prev))
        cnt.append(cntPrev)
        cover = cntPrev * prev + cover
        prev = v
        if cover >= m:
            break

    if cover < m:
        cntPrev = int(ceil((m - cover) / prev))
        cnt.append(cntPrev)

    print(sum(cnt))

for cntv,v in zip(cnt, l):
    print(f"{v} 取 {cntv}")