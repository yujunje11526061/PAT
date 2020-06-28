#!/usr/bin/env python
# -*- coding:utf-8 -*-

n = 1024-int(input())

cnt = 0
cnt += n>>6
n = n%64
cnt += n>>4
n = n%16
cnt += n>>2
n = n%4

print(cnt+n)
