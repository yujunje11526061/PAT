#!/usr/bin/env python
# -*- coding:utf-8 -*-

group =  int(input())

for _ in range(group):
    n = int(input())
    nums = sorted(map(int, input().split()), reverse=True)
    if(nums[1]+nums[2]>nums[0]):
        print("YES")
    else:
        print("NO")