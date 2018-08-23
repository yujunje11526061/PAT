#!/usr/bin/env.python
# -*- coding:utf-8 -*-
# !/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
贪心算法：
从起点开始探索极限距离内的加油站。有两种情况：
1. 范围内有比本地还便宜(或正好相等)的，则本地只加到正好到那里。能有便宜的坚决不多加。到那里之后重复此探索过程。
2. 范围内没有比本地还便宜的，则以范围内相对最便宜的点为目的地，本地加满油全力冲刺，没有更便宜的那我本地为啥不买满。到那里之后重复此探索过程
每一次探索得到的都是局部最优解和最优策略。且相互之间不冲突。
本题奇葩测试点：
1. 起点处没加油站，则一步也动不了
2. 在目的地外面还有加油站，无脑便宜。需要把终点作为一个虚拟站点加入。
3. 相同距离不同价格
4. 牛客网上有个坑点,终点前有个点价格为0
'''


class station():
    def __init__(self, dist, price):
        self.dist = dist
        self.price = price


volume, D, Davg, num = map(int, input().split())
limit = volume * Davg

l = []
for i in range(num):
    price, dist = map(float, input().split())
    l.append(station(dist, price))

l.append(station(D, 0))
l.sort(key=lambda i: (i.dist, i.price))  # 防止同距离不同价格,价格低的优先


def find_station(i, j):
    cnt = j
    lowest = l[j].price
    while l[j].dist - l[i].dist <= limit:
        if l[j].price <= l[i].price: # 牛客网上有个坑点,终点前存在一个点价格为0, 导致这边用小于号会一直往后搜直至越界,故用<=,对探索的推进不影响.
            cnt = j
            break
        if l[j].price < lowest:
            cnt = j
            lowest = l[j].price
        j += 1
    if l[cnt].dist - l[i].dist > limit:
        cnt = None
    return cnt


i = 0
tp, td = 0, 0
tank = 0  # 标记在每一个站点时油箱余量
flag = 1
if l[i].dist == 0:  # 起点有加油站才能出发
    while l[i].dist < D:
        j = i + 1
        next_station = find_station(i, j)
        if next_station is None:
            flag = 0
            td += limit
            break
        dist = l[next_station].dist - l[i].dist
        td += dist
        if l[next_station].price < l[i].price:
            tp += (dist / Davg - tank) * l[i].price  # 油箱余量一定不足以到达, 否则下一个点就成了上一个点的最优解了,没这个点啥事了
            tank = 0  # 到下一个点正好用完, 作为下一轮探索的初始值
        else:
            tp += (volume - tank) * l[i].price  # 加满油冲刺
            tank = volume - dist / Davg  # 到那里之后还剩多少,作为下一轮探索的初始值
        i = next_station
else:
    flag = 0
    td = 0

if flag == 0:
    print('The maximum travel distance = {:.2f}'.format(td))
else:
    print('{:.2f}'.format(tp))
