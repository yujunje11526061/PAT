#!/usr/bin/env.python
# -*- coding:utf-8 -*-
s = input()
n = len(s)

def find_symmetric_substring(s):
    if n == 1:
        return 1
    if n == 2:
        return 2 if s[0] == s[1] else 1
    i, j, k = 0, 1, 2
    maxlen = 2 if s[i]==s[j] else 1
    while k<= n-1:
        if s[k] == s[j]:
            l = 2
            p, q = j-1, k+1
            while p>=0 and q<=n-1:
                if s[p]==s[q]:
                    l +=2
                    p -= 1
                    q += 1
                else:
                    break
            if l > maxlen:
                maxlen = l
        if s[k] == s[i]:
            l = 3
            p, q = i-1, k+1
            while p>=0 and q<=n-1:
                if s[p]==s[q]:
                    l +=2
                    p -= 1
                    q += 1
                else:
                    break
            if l > maxlen:
                maxlen = l
        i,j,k = j,k,k+1
    return maxlen

print(find_symmetric_substring(s))



