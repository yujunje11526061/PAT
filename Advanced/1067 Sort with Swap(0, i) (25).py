#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
pat示例数据分两行，实际他妈是1行。
先扫描一遍，找出不匹配的数以及各个数各自站的位置
直接找0所占的位置该站的数。用0去换
如果0占了自己正确的位置，则弹出任一不配位的数和0换，重复上面步骤
'''
n, *l = map(int, input().split())


d = {}
outloc = set()
for i in range(len(l)):
    d[l[i]] = i
    if l[i] != i:
        outloc.add(l[i])
if len(outloc) ==0:
    print(0)
else:
    outloc.discard(0)
    count = 0
    while len(outloc)>0:
        while l[0] != 0:
            loc = d[0]
            x = loc
            locx = d[x]
            l[loc], l[locx] = l[locx], l[loc]
            d[0] = locx
            d[x] = loc
            try:
                outloc.remove(x)
            except:
                pass
            count+=1
        try:
            x = outloc.pop()
            l[0],l[d[x]] = l[d[x]], l[0]
            d[0],d[x] = d[x],0
            count +=1
        except:
            break
    print(count)