#!/usr/bin/env.python
# -*- coding:utf-8 -*-
stu, cou = map(int, input().split())
d = {}
for i in range(cou):
    id, num = map(int, input().split())
    if num == 0:
        continue
    names = input().split()
    for name in names:
        t = (((ord(name[0]) - ord('A')) * 26 + (ord(name[1]) - ord('A'))) * 26 + ord(name[2]) - ord('A')) * 26\
            + ord(name[3]) - ord('0')
        d.setdefault(t, []).append(id)

querys = input().split()
for name in querys:
    t = (((ord(name[0]) - ord('A')) * 26 + (ord(name[1]) - ord('A'))) * 26 + ord(name[2]) - ord('A')) * 26 \
        + ord(name[3]) - ord('0')
    course = d.get(t)
    if course is None:
        print(name, 0)
        continue
    course.sort()
    print(name, len(course), end = ' ')
    print(*course)