#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
l = list(map(int, input().split()))

# 此写法会超时，虽然这里是两遍遍历，最后一个小排序，但是对set的频繁操作也是费时的，只是比数组快一点而已
# s = set()
# leftmax = 0
# for i in l:
#     if i<leftmax:
#         continue
#     else:
#         leftmax = i
#         s.add(i)
#
# rightmin = 1000000001
# for j in l[::-1]:
#     if j>rightmin:
#         s.discard(j)
#     else:
#         rightmin = j
#
# print(len(s))
# print(*sorted(s))

# 此写法一次大排序加一轮遍历，不会超时。利用好快排每轮结束的主元的位置和最终相同这一特点。
h = sorted(l)
leftmax = 0
p = []
for i in range(n):
    e = l[i]
    if e<leftmax:
        continue
    elif e != h[i]:
        leftmax = e
    else:
        leftmax = e
        p.append(e)

print(len(p))
print(*p)