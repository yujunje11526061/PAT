#!/usr/bin/env.python
# -*- coding:utf-8 -*-
N = int(input())


class Book():
    def __init__(self, id, title, author, keywords, publisher, year):
        self.id = id
        self.title = title
        self.author = author
        self.keywords = keywords
        self.publisher = publisher
        self.year = year


'''
每个字段用一个字典来存储出现过的内容，内容作为Key，id组成的集合作为value
相比建类遍历的方法，空间换时间
不然会超时
'''
id = {}
title = {}
author = {}
keywords = {}
publisher = {}
year = {}
for cnt in range(N):
    i = input()
    t = input()
    title.setdefault(t, set()).add(i)
    a = input()
    author.setdefault(a, set()).add(i)
    k = set(input().split())
    for j in k:
        keywords.setdefault(j, set()).add(i)
    p = input()
    publisher.setdefault(p, set()).add(i)
    y = input()
    year.setdefault(y, set()).add(i)


# l = [Book(input(), input(), input(), set(input().split()), input(), input()) for i in range(N)]
#
# l.sort(key=lambda x: x.id)


def find_title(s):
    resp = sorted(title.get(s, []))
    if len(resp) > 0:
        for r in resp:
            print(r)
    else:
        print('Not Found')


def find_author(s):
    resp = sorted(author.get(s, []))
    if len(resp) > 0:
        for r in resp:
            print(r)
    else:
        print('Not Found')


def find_keywords(s):
    resp = sorted(keywords.get(s, []))
    if len(resp) > 0:
        for r in resp:
            print(r)
    else:
        print('Not Found')


def find_publisher(s):
    resp = sorted(publisher.get(s, []))
    if len(resp) > 0:
        for r in resp:
            print(r)
    else:
        print('Not Found')


def find_year(s):
    resp = sorted(year.get(s, []))
    if len(resp) > 0:
        for r in resp:
            print(r)
    else:
        print('Not Found')


query = {
    '1': find_title,
    '2': find_author,
    '3': find_keywords,
    '4': find_publisher,
    '5': find_year
}
M = int(input())
for i in range(M):
    x = input()
    num, describe = x.split(":")
    describe = describe.strip()
    print(x)
    query[num](describe)
