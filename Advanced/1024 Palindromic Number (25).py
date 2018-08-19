#!/usr/bin/env.python
# -*- coding:utf-8 -*-

def pn(x:str):
  return x == x[::-1]


n, k = input().split()
k = int(k)
count = 0
while count < k:
    if pn(n):
        break
    else:
        n = str(int(n) +int(n[::-1]))
        count += 1

print(n)
print(count)