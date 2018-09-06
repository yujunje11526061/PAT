#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
归并排序和插入排序的模板题。与1098 Insertion or Heap Sort 结合学习。
利用插入排序特征（未排序段同原始序列）判断时哪种排序的中间产物
归并中间产物没有用，根本不知道进行到哪一步了，请从头来。
'''

n = int(input())
l = list(map(int, input().split()))
h = list(map(int, input().split()))


flag = 'Merge Sort'
if h[0] > h[1]:
    print(flag)
    print(h[1], h[0])
else:
    i, j = 0, 1
    length = 1
    while j < n:
        if h[i] <= h[j]:
            length += 1
            i, j = j, j + 1
        else:
            break
    # 得知有序段的长度为length

# 此判断方法不对，应该利用插入排序的特点，有序段后面的应该和原序列相同！！
    # start, end = length, 2 * length - 1
    # while flag == 'Merge Sort' and start<n:
    #     for i in range(start, min(end, n - 1)):
    #         if h[i] > h[i + 1]:
    #             flag = 'Insertion Sort'
    #     start, end = end + 1, end + length
    flag = 'Insertion Sort' if h[length:]==l[length:] else flag

    if flag == 'Insertion Sort':
        i = length
        while i > 0 and h[i] <= h[i - 1]:
            h[i], h[i - 1] = h[i - 1], h[i]
            i -=1
        print(flag)
        print(*h)
    else: # 不要从中间序列开始，从上面得到的有序段length根本判断不出归并到哪一步了。直接从头来
        length = 1
        while length<n and l != h: # l != h应放在这里判断，这才是一轮归并
            start,end = 0, min(2*length, n)
            while start<n: # 这里只是一轮归并中的一次归并
                l[start:end] = sorted(l[start:end])
                start, end = end, min(end+2*length,n)
            length *= 2

        start, end = 0, min(2 * length, n)
        while start < n:
            l[start:end] = sorted(l[start:end])
            start, end = end, min(end + 2 * length, n)
        print(flag)
        print(*l)
