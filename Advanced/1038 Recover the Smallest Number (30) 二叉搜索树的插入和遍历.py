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
l.sort()
# print(l)
class node():
    def __init__(self, value, left = None, right = None):
        self.value =value
        self.left = left
        self.right = right


# 建立树类面向对象虽然可以较好地高内聚低耦合, 但是容易属性混乱..仅答题而言,直接写函数比较好.
class T():
    final = ''
    def __init__(self, root = None):
        self.root = root

    @classmethod
    def compare(cls, a: str, b: str):
        if a + b > b + a: #  插右边
            return False
        else: # 插左边
            return True

    def insert(self, other):
        p, pp = self.root, None # pp为p的父节点
        flag = 1
        while p is not None:
            if T.compare(p.value, other.value):
                pp = p
                p = p.right
                flag = 1
            else:
                pp = p
                p = p.left
                flag = 0
        if flag == 1:
            pp.right = other
        else:
            pp.left = other

    def inorder(self):
        T.final = ''
        T.inorder_transverse(self.root)

    @classmethod
    def inorder_transverse(cls, root):
        p = root
        if p is None:
            return
        T.inorder_transverse(p.left)
        T.final += p.value
        T.inorder_transverse(p.right)

tree = T(node(l[0]))

for elem in l[1:]:
    tree.insert(node(elem))

tree.inorder()

print(int(T.final))
