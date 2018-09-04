#!/usr/bin/env.python
# -*- coding:utf-8 -*-

def f():
    i = 3
    while 1:
        yield i
        i += 2


def judge(n):
    return lambda x: x % n > 0


def g():
    # yield 2
    it = f()
    while 1:
        p = next(it)
        yield p
        it = filter(judge(p), it)


# tt = g()
# while 1:
#     print(next(tt))

num = input()
print(num + '=', end='')
if num == '1':
    print(num)
else:
    num = int(num)
    generator = g()
    x = 2
    l = []
    s = ''
    while num > 1:
        if num % x == 0:
            l.append(x)
            num /= x
        else:
            if len(l) > 0:
                if len(l) == 1:
                    s += '{}*'.format(l[0])
                elif len(l) > 1:
                    s += '{}^{}*'.format(l[0], len(l))

            l = []
            x = next(generator)

    if len(l) > 1:
        s += '{}^{}'.format(l[0], len(l))
    elif len(l) == 1:
        s += '{}'.format(l[0])
    print(s)
