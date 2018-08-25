#!/usr/bin/env.python
# -*- coding:utf-8 -*-
card = [i + str(j) for i in ['S','H','C','D'] for j in range(1,14)]
card.extend(['J1','J2'])
# print(card)

times = int(input())
sf = list(map(int, input().split()))
card2 = [None]*54
# print(len(sf))
for i in range(times):
    for j in range(54):
        card2[sf[j]-1] = card[j]
    # 直接交换引用，类似归并排序里的并也可以并一次就交换引用，本质还是两个容器倒来倒去，但是写起来明了
    card, card2 = card2, card

print(*card)