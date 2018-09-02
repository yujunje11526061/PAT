# #!/usr/bin/env.python
# # -*- coding:utf-8 -*-
# M, N = map(int, input().split())
# l = map(int, input().split())
# pre = list(l)
# # io = sorted(l) # 不能这么写，迭代器是一次性的
# io = sorted(pre)
# s = set(io)
#
#  # 极度退化时递归会爆栈
# def pre_and_io(si, ei, sp, ep):
#     # if si>ei:
#     #     return
#     # if si == ei:
#     #     return
#     root = pre[sp]
#     if root == u:
#         print('{} is an ancestor of {}.'.format(u, v))
#     elif root == v and root != u:
#         print('{} is an ancestor of {}.'.fotmat(v, u))
#     else:
#         index = io.index(root)  # 可用二分法加速
#         length = index - si
#         if u < root and  v < root:  # 都在前半段（左子树）
#             pre_and_io(si, si + length - 1, sp + 1, sp + length)
#         elif u > root and  v > root:  # 都在后半段 （右子树）
#             pre_and_io(si + length + 1, ei, sp + length + 1, ep)
#         else:
#             print('LCA of {} and {} is {}.'.format(u, v, root))
#
#
# def find_LCA(u, v):
#     if u not in s and v not in s:
#         print('ERROR: {} and {} are not found.'.format(u, v))
#     elif u not in s:
#         print('ERROR: {} is not found.'.format(u))
#     elif v not in s:
#         print('ERROR: {} is not found.'.format(v))
#     else:
#         pre_and_io(0, N - 1, 0, N - 1)
#
#
# for i in range(M):
#     u, v = map(int, input().split())
#     find_LCA(u, v)
# ----------------------------------------------------------------------------------------
M, N = map(int, input().split())
l = map(int, input().split())
pre = list(l)
# io = sorted(l) # 不能这么写，迭代器是一次性的
io = sorted(pre)
s = set(io)

# 手写循环，碰到在极度退化的树，以及在末端的数据点还是会超时
def find_LCA(u, v):
    if u not in s and v not in s:
        print('ERROR: {} and {} are not found.'.format(u, v))
    elif u not in s:
        print('ERROR: {} is not found.'.format(u))
    elif v not in s:
        print('ERROR: {} is not found.'.format(v))
    else:
        si,ei,sp,ep = 0, N - 1, 0, N - 1
        while 0 <= si <= ei <= N - 1 and 0 <= sp <= ep <= N - 1:
            root = pre[sp]
            if root == u:
                print('{} is an ancestor of {}.'.format(u, v))
                return
            elif root == v and root != u:
                print('{} is an ancestor of {}.'.fotmat(v, u))
                return
            else:
                index = find_root(root, si,ei)  # 可用二分法加速
                length = index - si
                if u < root and v < root:  # 都在前半段（左子树）
                    si, ei, sp, ep = si, si + length - 1, sp + 1, sp + length
                elif u > root and v > root:  # 都在后半段 （右子树）
                    si, ei, sp, ep = si + length + 1, ei, sp + length + 1, ep
                else:
                    print('LCA of {} and {} is {}.'.format(u, v, root))
                    return

def find_root(root,si,ei):
    head,tail = si,ei
    while head<=tail:
        mid = (head+tail)//2
        if io[mid] == root:
            return mid
        elif io[mid] >= root:
            tail = mid-1
        else:
            head = mid+1
    return # 此题进入该函数必定能找到

for i in range(M):
    u, v = map(int, input().split())
    try:
        find_LCA(u, v)
    except:
        pass
# -----------------------------------------------------------------------------------------------
# M, N = map(int, input().split())
# l = map(int, input().split())
# pre = list(l)
#
# s = set(pre)
#
# def find_LCA(u, v):
#     if u not in s and v not in s:
#         print('ERROR: {} and {} are not found.'.format(u, v))
#     elif u not in s:
#         print('ERROR: {} is not found.'.format(u))
#     elif v not in s:
#         print('ERROR: {} is not found.'.format(v))
#     else:
#         for a in pre:   # 前序遍历的根先出现，故相等时的那个一定是另一个的根
#             if (a < u and a > v) or (a > u and a < v):  # u,v没有子孙关系的话，则必定在公共祖先两侧
#                 print('LCA of {} and {} is {}.'.format(u, v, a))
#                 break
#             elif a == u:
#                 print('{} is an ancestor of {}.'.format(u, v))
#                 break
#             elif a == v:
#                 print('{} is an ancestor of {}.'.format(v, u))
#                 break
# # 此写法对于极度退化的二叉树会超时，用递归写法则爆栈或超时
#
# for i in range(M):
#     u, v = map(int, input().split())
#     find_LCA(u, v)
