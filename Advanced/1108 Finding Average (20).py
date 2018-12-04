#!/usr/bin/env python
# -*- coding:utf-8 -*-
n = int(input())
l = input().split()

tot = 0
count = 0

for x in l:
    try:
        float(x)
    except:
        print(f"ERROR: {x} is not a legal number")
        continue
    ll = x.split(".")
    if len(ll)==1:
        y= int(x)
    elif len(ll)==2 and len(ll[1])<=2:
        y= float(x)
    else:
        print(f"ERROR: {x} is not a legal number")
        continue
    if -1000<=y<=1000:
        tot+=y
        count += 1
    else:
        print(f"ERROR: {x} is not a legal number")

if count==0:
    print("The average of 0 numbers is Undefined")
elif count==1:
    print("The average of {} number is {:.2f}".format(count, int(tot/count*100+0.5)/100))
else:
    print("The average of {} numbers is {:.2f}".format(count, int(tot / count * 100 + 0.5) / 100))