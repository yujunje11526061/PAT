#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
male = []
female = []
for i in range(n):
    name, gender, id, grade = input().split()
    grade = int(grade)
    if gender == 'M':
        male.append([grade, name, id])
    else:
        female.append([grade, name, id])

flag = 1
if len(female)>0:
    female.sort()
    print(*female[-1][1:])
    p = female[-1][0]
else:
    flag = 0
    print('Absent')

if len(male)>0:
    male.sort()
    print(*male[0][1:])
    q = male[0][0]
else:
    flag = 0
    print('Absent')

if flag:
    print(p-q)
else:
    print('NA')