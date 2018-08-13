#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, M = map(int, input().split())

l = [['01']]  # 按顺序记录每一代人没有孩子的人的id，不断读取数据和后续处理处理中更新
son = []
staged = []
for i in range(M):
    line = input().split()
    id = line[0]
    n = len(l)
    flag = 0
    for j in range(n):
        if id in l[j]:
            flag = 1
            l[j].remove(id)
            if j == n - 1:
                son.extend(line[2:])
            else:
                l[j + 1].extend(line[2:])

    if flag == 0:
        if id in son:
            son.remove(id)
            l.append(son)
            son = line[2:]
        else:  # 儿子比老子先出现,故在已经完成的树里没找到,flag为0,待进入树里的那一代人里也没, 先存起来
            staged.append(line)

l.append(son)


def loop(staged):
    if len(staged) > 0:
        for line in staged:
            id = line[0]
            flag = 0
            n = len(l)
            for j in range(n):
                if id in l[j]:
                    flag = 1
                    l[j].remove(id)
                    if j < n - 1:  # 同代人已经出现过了
                        l[j + 1].extend(line[2:])
                    else:  # 同代人中第一个出现的
                        l.append(line[2:])
                    staged.remove(line)

        loop(staged)
    else:
        return


loop(staged)
x = [str(len(i)) for i in l]

if N == 1 and M == 0:
    print(1)
else:
    print(" ".join(x))
