#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def method1():
    cnt = 0
    for line in sys.stdin:
        if (cnt == 0):
            n = int(line)
        if (cnt == 1):
            l = map(int, line.split())
        if (cnt == 2):
            flag = int(line)
        cnt += 1
        if (cnt == 3):
            l = sorted(l, reverse=flag)
            print(*l)
            cnt = 0


def method2():
    while (1):
        try:
            n = int(input())
            l = map(int, input().split())
            flag = int(input())
            l = sorted(l, reverse=flag)
            print(*l)
        except:
            break


method1()