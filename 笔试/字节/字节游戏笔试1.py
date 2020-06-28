#!/usr/bin/env python
# -*- coding:utf-8 -*-

while 1:
    try:
        length = int(input())
        linkedList = []
        for i in range(length):
            linkedList.append(int(input()))

        k = int(input())

        if k>=length:
            print("null")
        else:
            print(linkedList[-k-1])
    except:
        break