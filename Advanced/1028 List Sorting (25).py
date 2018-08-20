#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N, C = map(int, input().split())
if C == 1:
    l = []
    for i in range(N):
        id, name, score = input().split()
        id, score = int(id), int(score)
        l.append([id, name, score])
    l.sort()
    for id, name, score in l:
        print('{:0>6} {} {}'.format(id, name, score))
elif C == 2:
    l = []
    for i in range(N):
        id, name, score = input().split()
        id, score = int(id), int(score)
        l.append([name, id, score])
    l.sort()
    for name, id, score in l:
        print('{:0>6} {} {}'.format(id, name, score))
else:
    l = []
    for i in range(N):
        id, name, score = input().split()
        id, score = int(id), int(score)
        l.append([score, id, name])
    l.sort()
    for score, id, name in l:
        print('{:0>6} {} {}'.format(id, name, score))
