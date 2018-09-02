#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
对二叉树遍历的深入理解。利用好pre[head]==post[tail]来确定某一子树在遍历数组中的范围
什么情况不唯一，pre[head+1]==post[tail-1]时，即去掉根之后，又形成了前序头和末序尾一样的情况
又是一个以该相等值为根的子树，此时不能区分是左还是右
'''
N = int(input())
pre = list(map(int,input().split()))
post = list(map(int,input().split()))

class node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def judge(x,y,a,b): # x, y 对应前序，a，b对应后序
    global flag
    if x==y:
        return node(pre[x])
    if x>y:
        return
    root = pre[x]
    i,j = x+1,b-1
    if pre[i] == post[j]: # 表明整个子树在一边，且pre[i]为子树的根，可能左可能右，统一放左边，直接先判断一下这个免得后面扫太久
        flag = 'No'
        left = judge(i,y,a,j)
        return node(root,left)
    # 对后序从左往右扫，扫到第一个和pre[i]相等的就是左子树的范围
    p = a
    while p<j: # j-1已经上面判断过了
        if post[p] == pre[i]:
            break
        p += 1
    diff = p-a
    left = judge(i,i+diff, a,p)
    right = judge(i+diff+1, y, p+1,j)
    return node(root, left, right)

def inorder(t):
    if t is None:
        return
    inorder(t.left)
    io.append(t.value)
    inorder(t.right)

flag = 'Yes'
root = judge(0,N-1,0,N-1)
io = []
inorder(root)

print(flag)
print(*io)