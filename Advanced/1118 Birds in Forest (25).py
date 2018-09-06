#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
并查集模板题！！注意各个注释的细节！！
本题最大的鸟id即为鸟的数量，故并查集里无需记录个数
最好还是完整写一遍
'''
n = int(input())

father = [None] * 10010  # 记录每个成员所在集合的根，根的位置记录集合元素的个数，用负数表示


def find_father(x):
    if father[x] is None:  # 把新出现的成员在这里处理了，这样就不用在union()里分类讨论合到哪里了
        father[x] = -1
        return x
    elif father[x] < 0:
        return x
    else:
        root = find_father(father[x])  # 递归找根，这里最多105层，不会爆栈
        father[x] = root  # 递归每层返回前把当前的成员的父亲记录为总根，路径压缩！！
        return root


def union(a, b):
    fa, fb = find_father(a), find_father(b)
    if fa == fb:  # 同根直接返回
        return
    else:
        if father[fa] >= father[fb]:  # 负数记录，fb所在集合成员更多，小集并入大集
            father[fb] += father[fa]  # 先变成员总数，再变根！！！
            father[a], father[fa] = fb, fb
            return
        else:
            father[fa] += father[fb]
            father[b], father[fb] = fa, fa
            return


for i in range(n):
    num, *seq = map(int, input().split())
    try:  # 出现异常了再处理比每次去判断num为0为1要快
        a = seq[0]
        find_father(a) # 这一步很重要！！如果seq只有一个数，则a可能就没所属了！！
        for b in seq[1:]:
            union(a, b)
    except IndexError: # 以防num 为0
        continue
# 误！！！ 放循环里，生成器结束了不会抛出异常！！手动next()过头了就会抛出！还是不要随便用生成器取数了。

tree = 0
bird = 0
for f in father:
    if f is not None and f < 0:
        tree += 1
        bird -= f

print(tree, bird)
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    # print('Yes' if father[i] == father[j] else 'No')
    # 这样写就错啦，如果一个为另一个的根呢？如果两个各自为根又恰好成员数目一样呢
    print('Yes' if find_father(i) == find_father(j) else 'No')
