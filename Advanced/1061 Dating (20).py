#!/usr/bin/env.python
# -*- coding:utf-8 -*-
d = {'A':'MON', 'B':'TUE','C':'WED','D':'THU','E':'FRI','F':'SAT','G':'SUN'}
s1,s2,s3,s4 = input(),input(),input(),input()

l1,l2,l3,l4 = len(s1),len(s2),len(s3),len(s4)
def iscap(s):
    return ord('A')<=ord(s)<=ord('Z')
def islow(s):
    return ord('a')<=ord(s)<=ord('z')
i = 0
flag = []
flag2 = 1
while i< l1 and i <l2 and len(flag)<2:
    x,y = s1[i],s2[i]
    if len(flag)<1 and x == y and iscap(x) and ord(x)<=ord('G'):
        flag.append(x)
    elif len(flag)>0 and x == y:
        if iscap(x) and ord(x)<=ord('N'):
            flag.append(x)
            break
        try:
            flag.append(int(x))
            flag2 = 0
            break
        except ValueError:
            pass

    i += 1


day = d[flag[0]]
if flag2:
    hh = 9+ord(flag[1])-ord('A')+1
else:
    hh = '0'+str(flag[1])

j = 0
while j<l3 and j<l4:
    if s3[j] == s4[j] and (islow(s3[j]) or iscap(s3[j])):
        mm = j
        break
    j += 1
print("{} {}:{:0>2}".format(day, hh, mm))