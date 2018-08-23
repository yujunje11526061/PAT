#!/usr/bin/env.python
# -*- coding:utf-8 -*-

N, K = map(int, input().split())

root = {}
d = {}
g = set()


def find_root(elem):
    if root.get(elem) is None:
        return None
    while isinstance(root.get(elem), str):
        elem = root.get(elem)
    return elem


for i in range(N):
    x, y, t = input().split()
    t = int(t)
    d[x] = d.get(x, 0) + t
    d[y] = d.get(y, 0) + t
    rx, ry = find_root(x), find_root(y)
    if rx is None and ry is None:
        root[y] = x
        root[x] = [t, 2]
        total = root[x]
    elif rx is None and ry is not None:
        root[ry][0] += t
        root[ry][1] += 1
        total = root[ry]
        if d[y] > d[ry]:
            root[y] = total
            root[ry] = y
            root[x] = y
        else:
            root[x] = ry
    elif rx is not None and ry is None:
        root[rx][0] += t
        root[rx][1] += 1
        total = root[rx]
        if d[x] > d[rx]:
            root[x] = total
            root[rx] = x
            root[y] = x
        else:
            root[y] = rx
    else:
        if rx == ry:
            root[rx][0] += t
            total = root[rx]
            p = max([x, y, rx, ry], key=lambda i: d[i])
            root[x], root[y], root[rx], root[ry] = p, p, p, p
            root[p] = total
        else:
            total = [root[rx][0] + root[ry][0] + t, root[rx][1] + root[ry][1]]
            p = max([x, y, rx, ry], key=lambda i: d[i])
            root[x], root[y], root[rx], root[ry] = p, p, p, p
            root[p] = total
    if total[0] > K and total[1] > 2:
        pp = root[x]
        if isinstance(pp, str):
            g.add(pp)
        else:
            g.add(x)
g2 = set()
for j in g:
    pp = root[j]
    if isinstance(pp, str):
        g2.add(pp)
    else:
        g2.add(j)

print(len(g2))
l = sorted(g2)
for k in l:
    print(k, root[k][1])
