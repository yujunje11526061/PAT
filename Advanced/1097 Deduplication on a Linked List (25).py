#!/usr/bin/env.python
# -*- coding:utf-8 -*-
class node():
    def __init__(self, id, key, nextid):
        self.id = id
        self.key = key
        self.nextid = nextid
        self.abs = abs(key)
        self.flag = 0


s, n = map(int, input().split())
l = [None] * 100000
for _ in range(n):
    id, key, nextid = map(int, input().split())
    l[id] = node(id, key, nextid)

if l[s] is None:
    # print(None)
    pass
else:
    p = s
    pp = None
    record = set()
    ll = []
    while p != -1:
        this = l[p]
        if this.abs in record:
            ll.append(this)
            pp.nextid = this.nextid
            if not pp.flag and pp.nextid != -1:
                print('{:0>5} {} {:0>5}'.format(pp.id, pp.key, pp.nextid))
                pp.flag = 1
            p = this.nextid
        else:
            record.add(this.abs)
            if pp is not None and not pp.flag:
                print('{:0>5} {} {:0>5}'.format(pp.id, pp.key, pp.nextid))
                pp.flag = 1
            pp = this
            p = this.nextid
    print('{:0>5} {} {}'.format(pp.id, pp.key, -1))

    if len(ll) != 0:
        for i in range(len(ll) - 1):
            this = ll[i]
            nextone = ll[i + 1]
            print('{:0>5} {} {:0>5}'.format(this.id, this.key, nextone.id))

        print('{:0>5} {} {}'.format(ll[-1].id, ll[-1].key, -1))
