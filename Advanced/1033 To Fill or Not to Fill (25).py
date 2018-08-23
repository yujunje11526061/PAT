#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
切分法，找到路径上价格递减(准确说,非递增,因为会有终点前有个站点免费的坑点)的点，这是必经点，到达这些点必然是空仓的，将总路径进行划分成多段，从起点开始逐段考虑
如果该段长度不大于上限长度（满仓能跑的距离limit），则只加恰好跑到那里的量。费用和路径长度不难计算。
如果该段长度大于上限长度，则调用一个plan(head, tail)函数来处理这一段，需要在中间找中转点（transfer）。将该段再划分成两段。依次考虑。
中转点的选择标准为：该段中，最便宜的点（不包括头尾），若无，则返回None，表明无中转点可以补油，旅行终止

plan函数中引入一个临时变量left。表明再该段中，我在起点head加满油，跑到最大距离head+limit，距离目标点tail还剩多少距离，即 left = tail-head-limit
这个余量left，就是我需要在中转站中补油来cover掉的。
plan函数中主循环条件为left>0，直到全部cover掉或者找不到中转站，旅行被迫中止。循环过程中实时更新本段累计价格p和距离d，最后最为函数返回值。若旅行被迫中止，则p作为中止的标记
然后分为三种情况：
1. 中转站可以cover掉所有left，皆大欢喜。直接算出left这部分钱就行
2. 中转站太近了，油箱余量所能补的油只能cover一部分left。则把中转站作为新起点head = transfer，left = left -covered，继续循环
3. 中转站太远了，到达中转点的距离仍过大，则出现同性质的子问题，可递归求解plan(head, transfer)。 进一步深入找中转站。

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
l.sort(key=lambda i: (i.dist, i.price))


stop = [] # 记录那些必经点，包括起点和终点
cnt = 0
for i in range(num+1):
    if l[i].price <= l[cnt].price:
        stop.append(i)
        cnt = i
        if l[cnt].dist >= D: # 到终点了就跳出
            break
if l[stop[-1]].dist<D:
    stop.append(num)

# print(stop)
def find_lowest(m, n):
    if n-m == 1:
        return None
    k = m + 1
    lowest = l[k].price
    transfer = k
    while k < n:
        if l[k].price < lowest:
            lowest = l[k].price
            transfer = k
        k += 1
    return transfer


def plan(s, e):  # s, e为l中的坐标, 且s-e>1
    left = l[e].dist - l[s].dist - limit
    p = 0
    d = 0
    while left > 0:  # 能成功cover掉超限的那部分，才能正常返回
        transfer = find_lowest(s, e)
        if transfer is None:
            return None, limit+d # 旅行中止按题意要加上垂死挣扎的距离
        covered = l[transfer].dist - l[s].dist
        if covered <= limit:  # 中转站距离不超限
            if covered >= left: # 全部cover掉
                p += left*l[transfer].price/Davg
                d += left
                return p, d
            else:  # 中转站太近，不能完全cover掉
                left -= covered
                s = transfer
                p += covered*l[transfer].price/Davg
                d += covered
        else: # 中转站太远，产生同类子问题，进一步找中转站，递归求解。
            p_, d_ = plan(s, transfer)
            d += d_
            if p_ is None:
                return None, d
            p += p_
            left -= d_
            s = transfer
    return p, d


i = 0
j = 1
tp = 0
td = 0
if l[i].dist == 0:  # 起点有加油站才能出发
    while j < len(stop):  # i, j为必经点stop中的坐标， stop中的坐标为所有点l中的元素
        dd = l[stop[j]].dist - l[stop[i]].dist
        if dd <= limit:
            td += dd
            tp += dd * l[stop[i]].price / Davg
            p = 1
        elif stop[j] - stop[i] == 1: # 直接把相邻两站的距离超限的情况过滤掉了
            td += limit
            p = None
            break
        else: # 非相邻两站距离超限，找中转站
            tp += limit * l[stop[i]].price / Davg # 这部分距离是必跑的，plan函数中只需要考虑left中能跑多少就行
            p, d = plan(stop[i], stop[j])
            if p is None:
                td += d
                break
            tp += p
            td += d
        i += 1
        j += 1
else:
    p = None
    td = 0

if p is None:
    print('The maximum travel distance = {:.2f}'.format(td))
else:
    print('{:.2f}'.format(tp))
