#!/usr/bin/env.python
# -*- coding:utf-8 -*-
# !/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
初始对币种排序，便于穷举时能按照一定的优先度取。取的操作抽象为移动数组下标的变化。币规模减少一枚即数组下标+1
穷举法，并使最小的序列先递归，出现合适的就一直return True跳出最外层函数
'''
N, M = map(int, input().split())
l = sorted(map(int, input().split()))


def package_problem(s, tot, seq):
    global count
    if s > N - 1:  # 币用完都凑不够
        return False
    elif l[s] > tot:  # 往后再取一枚必就超出了
        return False
    elif l[s] == tot:  # 正好凑够.  若要输出所有结果以及个数，只需要再真正的出口输出就好了
        seq.append(l[s])
        print(seq)
        seq.pop()
        count += 1
        return count
    ## 0-1背包，多重背包，同一币种数量有限，类似本题是多重背包，直接对所有币排序，然后从数组取就是
    ## 如果是完全背包，即每个币种无限量，则外面套循环，总量依次减去l[s],直到小于0，因为每个币种最多取tot/face_value个
    seq.append(l[s]) # 更新已探知序列状态进入下一轮探索
    package_problem(s + 1, tot - l[s], seq)  # 若算上下一枚币，则币规模减少，问题规模也减少
    seq.pop() # 回溯后恢复状态.更新再回复可以避免每次递归时复制序列带来的内存和时间开销.
    package_problem(s + 1, tot, seq)  # 若不算下一枚币，则币规模减少，问题规模不变

    return count


seq = []
count = 0
if sum(l) < M:
    print('No Solution')
elif package_problem(0, M,seq):
    print(count)
else:
    print('No Solution')
