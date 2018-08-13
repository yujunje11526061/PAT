#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, M = map(int, input().split())

class Student():
    def __init__(self,id, c, m, e):
        self.id = id
        self.c = c
        self.m = m
        self.e = e
        self.a = (c+m+e)/3


d = {}
s = []
for i in range(N):
    id, *ll = input().split()
    s.append(Student(id, *[int(j) for j in ll]))
    d[id] = s[i]

ID = [input() for i in range(M)]

# print(s)

obj = ['A','C','M','E']
d2 = {'a':0, 'c':1,'m':2, 'e':3}
for attr_name in d2.keys():
    s.sort(key=lambda x:x.__getattribute__(attr_name), reverse=True)  # 列表的sort()方法返回None！！！！是就地修改！！！！
    rank = 1
    score = s[0].__getattribute__(attr_name)
    for i in range(N):
        stu = s[i]
        if stu.__getattribute__(attr_name) < score:
            rank = i + 1
            score = stu.__getattribute__(attr_name)
        stu.__setattr__(attr_name+'rank', (rank, d2[attr_name])) # 把科目的优先级作为元组的第二个元素，即第二级排序键

# s.sort(key=lambda x:x.a, reverse=True)  # 列表的sort()方法返回None！！！！是就地修改！！！！
# rank = 1
# score = s[0].a
# for i in range(N):
#     stu = s[i]
#     if stu.a < score:
#         rank = i + 1
#         score = stu.a
#     stu.arank = (rank, 0)  # 把科目的优先级作为元组的第二个元素，即第二级排序键
#
# s.sort(key=lambda x:x.c, reverse=True)
# rank = 1
# score = s[0].c
# for i in range(N):
#     stu = s[i]
#     if stu.c < score:
#         rank = i + 1
#         score = stu.c
#     stu.crank = (rank, 1)
#
# s.sort(key=lambda x: x.m, reverse=True)
# rank = 1
# score = s[0].m
# for i in range(N):
#     stu = s[i]
#     if stu.m < score:
#         rank = i + 1
#         score = stu.m
#     stu.mrank = (rank, 2)
#
# s.sort(key=lambda x:x.e, reverse=True)
# rank = 1
# score = s[0].e
# for i in range(N):
#     stu = s[i]
#     if stu.e < score:
#         rank = i + 1
#         score = stu.e
#     stu.erank = (rank, 3)

def find_rank(id):
    stu = d.get(id, None)
    if stu is None:
        return ('N/A', None)

    rank, subj_num = sorted([stu.arank, stu.crank, stu.mrank, stu.erank])[0]
    subject = obj[subj_num]
    return (rank, subject)

for id in ID:
    rank, subject = find_rank(id)
    print(rank, subject) if subject is not None else print(rank)
