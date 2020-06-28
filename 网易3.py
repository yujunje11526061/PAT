#!/usr/bin/env python
# -*- coding:utf-8 -*-

def compare(a,b):
    if str(a)+str(b) < str(b)+str(a):
        return True
    else:
        return False


class node:
    def __init__(self,val):
        self.val = val

    def __lt__(self, other):
        return compare(self.val, other.val)

    def __repr__(self):
        return str(self.val)

n = int(input())
nums = list(map(int,input().split()))
oddOrEven = nums[0]&1
flag = True
for num in nums[1:]:
    if(oddOrEven != (num&1)):
        flag = False
        break

if flag: # 全奇数或全偶数
    print(*nums)
else:
    nodes = [node(num) for num in nums]
    nodes.sort()
    print(*nodes)

