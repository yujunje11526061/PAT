#!/usr/bin/env.python
# -*- coding:utf-8 -*-
n = int(input())

preorder = []
inorder = []
stack = []
for i in range(2*n):
    s = input().split()
    if len(s)>1:
        preorder.append(int(s[-1]))
        stack.append(int(s[-1]))
    else:
        inorder.append(stack.pop())

post = []
# print(inorder, preorder)
def postorder(si,ei,sp,ep):  # 函数中的起点终点都用代号表示！！
    global post
    if si>ei:
        return
    if si == ei:
        post.append(inorder[si])
        return
    root = preorder[sp]
    index = inorder.index(root)
    l = index - si
    postorder(si, si+l-1, sp+1, sp+l)
    postorder(si+l+1, ei, sp+l+1, ep)
    post.append(root)

postorder(0, n-1, 0, n-1)
print(*post)
