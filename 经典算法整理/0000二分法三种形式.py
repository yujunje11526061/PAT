#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
l数组存储非减序列，在坐标s和e之间对值x进行查找，返回坐标。
分为找到找不到，找不到好办
找不到的情况下，一定是此种关系结束，若：x < l[s], 则tail = s-1 越界，x > l[e], 则head = e+1 越界.
找到的情况下：
1. 序列不重复，则直接返回mid坐标，用find函数
2. 序列有重复，要找最大坐标，则循环必定走完，最终tail是最大坐标，find_max函数。
3. 序列有重复，要找最小坐标，则循环必定走完，最终head是最小坐标，find_min函数。
循环条件一定是 s <= head <= tail <= e
头尾更新一定是head = mid + 1 或 tail = mid - 1
找最大坐标，相等情况归入head的更新，找最小坐标，相等的情况归入tail的更新
'''


def find(s, e, x):
    head, tail = s, e
    while s <= head <= tail <= e:
        mid = (head + tail) // 2
        if l[mid] == x:
            return mid
        if l[mid] < x:
            head = mid + 1
        else:
            tail = mid - 1
    return 'l[tail] < x < l[head] and tail + 1 = head'
    # 找不到的情况下，一定是此种关系结束，若：x < l[s], 则tail = s-1 越界，x > l[e], 则head = e+1 越界.


def find_max(s, e, x):
    head, tail = s, e
    while s <= head <= tail <= e:
        mid = (head + tail) // 2
        if l[mid] <= x:
            head = mid + 1
        else:
            tail = mid - 1
    return  tail
    # x = l[tail] < l[head]
    # 找到时，tail 是要找到时的最大坐标， 找不到的情况同 find


def find_min(s, e, x):
    head, tail = s, e
    while s <= head <= tail <= e:
        mid = (head + tail) // 2
        if l[mid] >= x:
            tail = mid - 1
        else:
            head = mid + 1
    return head
    # l[tail] < l[head] = x
    # 找到时，head 是要找到时的最小坐标， 找不到的情况同 find
