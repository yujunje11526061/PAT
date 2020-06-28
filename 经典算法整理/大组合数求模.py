#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scipy.special import comb
import math

'''
求大组合数C(m,n)对p取模的值
'''
m, n, p = 3000000, 30000, int(1e9 + 7)
# C(m,n,p) = C(m//p,n//p)*C(m%p, n%p)%p Lucas定理，当m和n很大时用
# (a/b)%p = a*(b**(p-2))%p 费马小定理
# C(m,n,p) = (m!/(n!*(m-n)!))%p = m!* ((n!*(m-n)!))**(p-2) % p
# x = m!
# y = n!
# z = (m-n)!
# 则C(m,n,p) = x*((y*z)**(p-2))%p
x,y,z = 1,1,1

for i in range(1, m+1): # 递推求阶乘
    x = x*i%p
    if i==n:
        y = x
    if i == m-n:
        z = x
a,b = x, y*z%p

def quickPow(base, exp, mod):
    '''
    基于循环和位运算的快速幂求法
    把exp看成二进制表示。
    :param base:
    :param exp:
    :param mod:
    :return:
    '''
    result = 1
    while exp:
        if exp&1:
            result = result*base%mod
        base = base*base%mod
        exp = exp>>1 # 移位运算时返回一个新的数！！
    return result

def calculate(s,e):
    result = 1
    while s>=e>0:
        result *= s
        s -= 1
    return result

print(f"C(m,n,p) m取n的组合数对p取模\nm = {m}, n = {n}, p = {p}\n")
print("基于费马小定理和快速幂算：","\n此法快速且最准确，以下两种不准确，且会溢出")
print(a*quickPow(b,p-2,p)%p if m>=n else 0, end="\n\n")
# print("利用阶乘硬算：")
# print(int((calculate(m,m-n+1)/calculate(n,1)))%p if m>=n else 0,end="\n\n")
# print("利用Scipy包算：")
# print(int(comb(m,n))%p)



