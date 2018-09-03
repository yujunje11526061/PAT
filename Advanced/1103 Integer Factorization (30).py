#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
均值不等式，全相等时和最大。也是枚举的下届，从而可以保证序列是非增的
'''
N, K, P = map(int, input().split())
def f(x):
    return x**P

final = [0]*K
maxsum = 0

def find(tot, num, xl):
    global final, maxsum
    x = int((tot / num) ** (1 / P))
    if f(x)*num == tot:
        xl = xl+[x]*num
        s = sum(xl)
        if s > maxsum:
            maxsum = s
            final = xl
            return
        # elif s == maxsum and xl > final: # 可以不用，非增序列，从大到小枚举，先找到的一定是最大的序列
        #     final = xl
        return
    start = int(tot**(1/P)) # 枚举的上届
    if f(start) == tot:
        start -= 1
    for i in range(start,x,-1):
        find(tot-f(i), num-1, xl+[i])


if N-K<3 and N!=K:
    print('Impossible')
else:
    find(N,K,[])
    if final == [0]*K:
        print('Impossible')
    else:
        s1 = '{} ='.format(N)
        s2 = ' + '.join(['{}^{}'.format(final[i], P) for i in range(K)])
        print(s1, s2)
