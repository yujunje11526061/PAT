#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
仔细读题。。注意单复数。。
'''
n = int(input())
dc = {
    '0':'%',
    '1':'@',
    'l':'L',
    'O':'o'
}
def change(s):
    ns = ''
    flag = 0
    for i in s:
        if i in dc:
            flag = 1
            i = dc[i]
        ns += i
    if flag == 0:
        return None
    else:
        return ns
count = 0
l = []
if n == 1:
    input()
    print('There is 1 account and no account is modified')
else:
    for i in range(n):
        name, s = input().split()
        s = change(s)
        if s is None:
            continue
        l.append([name, s])
        count += 1

    if count == 0:
        print('There is {} accounts and no account is modified'.format(n))
    else:
        print(count)
        for elem in l:
            print(*elem)