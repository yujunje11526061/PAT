#!/usr/bin/env.python
# -*- coding:utf-8 -*-

'''
另一种意义上的排序
字符串a+b > b+a, a>b ,反之则b>=a
解法1:自己手写排序, 只不过比较方法是新式的大小于.
时间复杂度: O(NlogN), 不考虑输入输出的整合和a+b>b+a这一原子操作
解法2:由于a,b的相对位置不变, 一系列字符串存在一个相对位置,符合二叉搜索树的特征. 题意想要的从小到大输出,其实就是中序遍历
时间复杂度: 插入O(NlogN), 遍历O(N) 不考虑输入输出的整合和a+b>b+a这一原子操作
实测也是解法一直接排序更快点.
'''

l = input().split()
N = int(l[0])
l = l[1:]

class STR(str):
    @classmethod
    def compare(cls, a, b):
        if super().__lt__(a + b, b + a): #  a>b
            return True
        else: # a<b
            return False
    def __lt__(self, other):
        if STR.compare(self, other):
            return True
        else:
            return False

# 关键在于重新定义大小比较的规则,然后直接调用Tim排序即可.
l = sorted(map(STR, l))
print(int(''.join(l)))