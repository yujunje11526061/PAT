#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
考察进制转换和素数判断
'''
from math import sqrt

# print(to_ten(1111111,2))

def to_radix_reverse_to_ten(number, radix):
    if radix == 10:
        return int(str(number)[::-1])
    s = []
    while number>0:
        s.append(number%radix)
        number = number//radix
    for i in s:
        number = radix * number + int(i)
    return number


def is_prime(number):
    if number == 1:
        return False
    limit = int(sqrt(number))
    for i in range(2, limit+1):
        if number%i == 0:
            return False
    return True

# for i in [73,3,5,7,8,9,37,55,100]:
#     print(is_prime(i))

while 1:
    xx = input().split()
    if len(xx) == 1:
        break
    number = int(xx[0])
    radix = int(xx[1])
    if is_prime(number) and is_prime(to_radix_reverse_to_ten(number, radix)):
        print('Yes')
    else:
        print('No')