#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())
init = list(map(int, input().split()))
seq = list(map(int, input().split()))

for i in range(n - 1):
    if seq[i] <= seq[i + 1]:
        i += 1
    else:
        break

if seq[i + 1:] == init[i + 1:]:
    print('Insertion Sort')
    i += 1
    while i > 0:
        if seq[i] < seq[i - 1]:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1
        else:
            break
    print(*seq)
else:
    print('Heap Sort')
    head, tail = 0, n - 1
    while 0 <= head <= tail <= n - 1:
        mid = (head + tail) // 2
        if seq[mid] >= seq[0]:
            tail = mid - 1
        else:
            head = mid + 1
    size = head  # 剩余堆的大小，末尾坐标为size-1
    x = seq[size - 1]
    seq[size - 1] = seq[0]
    size -= 1
    # 最大堆的siftdown操作
    i, j = 0, 2 * i + 1
    while j < size:
        if j + 1 < size and seq[j] < seq[j + 1]:
            j = j + 1
        if x >= seq[j]:
            break
        else:
            seq[i] = seq[j]
        i, j = j, 2 * i + 1
    seq[i] = x
    print(*seq)
