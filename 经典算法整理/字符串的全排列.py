#!/usr/bin/env python
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
本质上是一个完全连通无向图所有遍历路径问题
DFS+回溯法

此解法利用了换头，来保证不会重复访问
'''

class Permutation:
    def permutation(self, ss):
        # write code here
        if len(ss) == 0:
            return []
        self.ls = list(ss)
        self.length = len(ss)
        self.table = []
        self.path = []
        self.set_ = set()
        self.find(0)
        self.table.sort()
        return self.table

    def find(self, now:"当前子串在总串中的首位置"):
        if now == self.length:
            string = "".join(self.path)
            if string not in self.set_:
                self.set_.add(string)
                self.table.append(string)
        for i in range(now, self.length):
            # 依次让当前子串中的每个字符做头，变成 头 + 后面子串的全排列 问题
            self.ls[i], self.ls[now] = self.ls[now], self.ls[i]
            self.path.append(self.ls[now])
            self.find(now + 1) # 递归求解下一个位置
            # 回退
            self.path.pop()
            self.ls[i], self.ls[now] = self.ls[now], self.ls[i]

class Combination:
    def combination(self, ss):
        self.ss = ss
        self.length = len(ss)
        self.table = []
        self.set_ = set()
        self.find(0,"")
        self.table.sort(key= len)
        return

    def find(self, now, cnt_ss):
        for head in range(now,self.length):
            s = cnt_ss+self.ss[head]
            if s not in self.set_:
                self.set_.add(s)
                self.table.append(s)
            self.find(head+1, s)

solution1 = Permutation()
solution1.permutation("abc")
print(solution1.table)
solution2 = Combination()
solution2.combination("abc")
print(solution2.table)