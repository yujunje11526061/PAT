#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = int(input())

def do():
    string = input()
    stack = []
    pre = ''
    preCnt = 0
    prePre = ''
    prePreCnt = 0
    for s in string:
        if s==pre:
            if preCnt==2:
                continue
            elif prePreCnt==2:
                continue
            else:
                preCnt += 1
                stack.append(s)
        else:
            stack.append(s)
            prePre = pre
            pre = s
            prePreCnt = preCnt
            preCnt = 1

    print("".join(stack))
    return

for i in range(n):
    do()