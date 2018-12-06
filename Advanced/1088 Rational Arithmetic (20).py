#!/usr/bin/env python
# -*- coding:utf-8 -*-
x, y = input().split()
x1, x2 = map(int, x.split("/"))
y1, y2 = map(int, y.split("/"))
fx = "-" if x[0] == "-" else "+"
fy = "-" if y[0] == "-" else "+"


def findmax(a, b):
    a,b = abs(a),abs(b)
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    while b % a != 0:
        a, b = b % a, a
    return a


mx = findmax(x1, x2)
my = findmax(y1, y2)
x1, x2 = x1 / mx, x2 / mx
y1, y2 = y1 / my, y2 / my


def foroutput(a, b, f):
    a, b = int(abs(a)), int(abs(b))
    s = ""
    if a == 0:
        return "0"
    if b == 1:
        s += str(a)
        if f == "-":
            return "(-" + s + ")"
        return s
    elif a > b:
        s = s + str(a // b) + " "
        a = a % b
    s = s + str(a) + "/" + str(b)
    if f == "-":
        return "(-" + s + ")"
    return s


i1, i2 = x1 * y2 + x2 * y1, x2 * y2
mi = findmax(i1,i2)
i1,i2 = i1/mi,i2/mi
fi = "-" if x1 / x2 + y1 / y2 < 0 else "+"
print(foroutput(x1, x2, fx), "+", foroutput(y1, y2, fy), "=", foroutput(i1, i2, fi))

j1, j2 = x1 * y2 - x2 * y1, x2 * y2
mj = findmax(j1,j2)
j1,j2 = j1/mj,i2/mj
fj = "-" if x1 / x2 - y1 / y2 < 0 else "+"
print(foroutput(x1, x2, fx), "-", foroutput(y1, y2, fy), "=", foroutput(j1, j2, fj))

k1, k2 = x1 * y1, x2 * y2
mk = findmax(k1,k2)
k1,k2 = k1/mk,k2/mk
fk = "-" if fx != fy else "+"
print(foroutput(x1, x2, fx), "*", foroutput(y1, y2, fy), "=", foroutput(k1, k2, fk))

l1, l2 = x1 * y2, x2 * y1
ml = findmax(l1,l2)
l1,l2 = l1/ml,l2/ml
fl = "-" if fx != fy else "+"
if y1 == 0:
    print(foroutput(x1, x2, fx), "/", foroutput(y1, y2, fy), "= Inf")
else:
    print(foroutput(x1, x2, fx), "/", foroutput(y1, y2, fy), "=", foroutput(l1, l2, fl))
