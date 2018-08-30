#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
初始对币种排序，便于穷举时能按照一定的优先度取。取的操作抽象为移动数组下标的变化。
穷举法，并使符合题意优先级的序列先递归，出现合适的就一直return True跳出最外层函数
'''
N,M = map(int, input().split())
l = sorted(map(int, input().split()))

def backage_problem(s, tot):
    global seq
    if s>N-1: # 币用完都凑不够
        return False
    elif l[s]> tot: # 往后再取一枚必就超出了
        return False
    elif l[s] == tot: # 正好凑够
        seq.append(l[s])
        return True
    elif backage_problem(s+1, tot-l[s]): # 当前最小面额算上能凑够，则币规模减少，问题规模也减少
        seq.append(l[s])
        return True
    elif backage_problem(s+1, tot): # 当前最少面额算上凑不够，则币规模减少，问题规模不变
        return True
    else:
        return False

seq = []
if sum(l)<M:
    print('No Solution')
elif backage_problem(0, M):
    print(*seq[::-1])
else:
    print('No Solution')
