#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
前序中序转后序
递归写法会爆栈
掌握此类问题如何手写栈，以及根的处理，是否压栈的判断，压栈顺序的处理
index = io.index(root) 该方法是顺序扫描的，这里可用字典优化（如果内存允许），对于搜索树可以二分法优化
加速点：
1.post有东西了直接跳出。手写栈可以直接跳出循环而递归只能一层层返回
2.用字典存储中序中每个东西的下标，这样方便迅速定位根
'''
N = int(input())
pre = list(map(int, input().split()))
io = list(map(int, input().split()))
d = {io[i]: i for i in range(N)}

# # 递归会爆栈
# def pre_and_io(si, ei, sp, ep):
#     if si > ei or len(post) > 0:  # 只要后序有东西了，就可以提前退出
#         return
#     if si == ei:
#         return post.append(io[si])
#     root = pre[sp]
#     index = d[root]
#     length = index - si
#     pre_and_io(si, index - 1, sp + 1, sp + length)
#     pre_and_io(index + 1, ei, sp + length + 1, ep)
#     post.append(root)


post = []
# pre_and_io(0, N - 1, 0, N - 1)
stack = [(0, N - 1, 0, N - 1)]
while len(stack) > 0:
    si, ei, sp, ep = stack.pop()
    if si == ei:  # 虽然相等的情况在压栈前已经处理掉了，但是这是为了处理根，认为地让他前后相等
        post.append(io[si])
    if len(post) > 0:  # 只要后序有东西了，就可以提前退出
        break
    root = pre[sp]
    index = d[root]
    length = index - si
    # 后序遍历根在最后，先压栈，注意压栈的形式，方便出栈时处理
    # 否则就要判断他的子树是否压栈，都不压栈则根直接输出，任一个压栈则根要先压栈
    # 直接写成前后相等的形式，不管子树进不进栈根都进栈，只要在出栈时对前后相等的情况进行处理
    # 而子树中出现前后坐标相等的情况就不压栈了，直接下面输出
    stack.append((sp, sp, index, index))
    si1, ei1, sp1, ep1 = si, index - 1, sp + 1, sp + length
    si2, ei2, sp2, ep2 = index + 1, ei, sp + length + 1, ep
    # 右子树要比左子树先压栈
    # 等于的情况可以直接加到post里，虽然可以压栈，在下一次出栈的时候再处理，这样多了一轮压栈出栈的开销
    if si2 < ei2:
        stack.append((si2, ei2, sp2, ep2))
    elif si2 == ei2:
        post.append(io[si2])
    if si1 < ei1:
        stack.append((si1, ei1, sp1, ep1))
    elif si1 == ei1:
        post.append(io[si1])

print(post[0])
