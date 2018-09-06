#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n, k = map(int, input().split())
l = [None]*n
for i in range(n):
    name,h = input().split()
    h = int(h)
    l[i] = (-h, name)
l.sort()
num, left = divmod(n,k)
numforeach = [num]*k
numforeach[0] += left
i = 0
for r in range(k):
    j = numforeach[r]
    row = [None]*j
    temp = l[i:i+j]
    if j == 1:
        print(temp[0][1])
        i += j
        break
    myleft = temp[1::2] # 直接利用列表切片取出两边的人，也可以自己利用数组存，而不是一个个去放，center这个条件就是干扰信息
    myleft.reverse()
    myleft = [i[1] for i in myleft]
    myright = temp[::2]
    myright = [i[1] for i in myright]
    print(*myleft,*myright)
    i += j

