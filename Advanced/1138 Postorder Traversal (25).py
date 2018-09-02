#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N = int(input())
pre = list(map(int, input().split()))
io = list(map(int, input().split()))

def pre_and_io(si,ei,sp,ep):
    if si > ei or len(post)>0: # 只要后序又东西了，就可以提前退出
        return
    if si == ei:
        return post.append(io[si])
    root = pre[sp]
    index = io.index(root)
    length = index-si
    pre_and_io(si, index-1, sp+1, sp+length)
    pre_and_io(index+1,ei, sp+length+1, ep)
    post.append(root)


if pre == io:
    print(io[-1])
elif pre == io[::-1]:
    print(io[0])
else:
    post = []
    pre_and_io(0,N-1,0,N-1)
    print(post[0])