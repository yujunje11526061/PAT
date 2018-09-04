#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
l = []
for i in range(n):
    name, id, grade = input().split()
    grade =int(grade)
    l.append([grade, name,id])

l.sort()

s,e = map(int, input().split())

def find_loc(x): #  所有分数都不同的，这样好办
    head,tail = 0,n-1
    while head<=tail:
        mid = (head+tail)//2
        if l[mid][0] == x:
            return mid if x==s else mid+1
        elif l[mid][0] > x:
            tail = mid-1
        else:
            head = mid+1
    return head

if s<e:
    start, end = find_loc(s), find_loc(e)
    l = l[start:end]
    if len(l)>0:
        for item in l[::-1]:
            print(*item[1:])
    else:
        print('NONE')
elif s>e:
    print('NONE')
else:
    loc = find_loc(s)
    if l[loc][0] == s:
        print(*l[loc][1:])