#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import Thread
import threading
def a():
    print("A",end="")
def b():
    t=Thread(target=a)
    t.start()
    t.join()
    print("B",end="")
def c():
    t=Thread(target=b)
    t.start()
    t.join()
    print("C",end="")
def d():
    t=Thread(target=c)
    t.start()
    t.join()
    print("D",end="")

while 1:
    try:
        n = int(input())
        for i in range(n):
            d()
        print("")
    except:
        break