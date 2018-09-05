#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
字符串处理较难题
思路不对，应该从做开始扫描找小数点位置以及第一个非零数的位置
按照有无小数点，整数部分是否为0（决定正次方还是副次方）分类处理，直接生成最终字符串，再比较
而不是分析各种可能的细节
'''
n, s1, s2 = input().split()
n = int(n)
s1,s2 = s1.lstrip('0'), s2.lstrip('0')
xx = []
for s in (s1,s2):
    x = ''
    i = 0
    cnt = 0
    point = None
    pnot0 = None
    while i<len(s):
        if s[i] =='.':
            if len(x)==0:
                x = '0.'
                point = 1
                cnt += 1
            else:
                x += '.'
                point = cnt
        elif s[i] == '0':
            x += s[i]
            cnt += 1
        else:
            if pnot0 is None:
                pnot0 =  len(x)
            x += s[i]
            cnt += 1

        i += 1

    if point is None:
        if len(x)<n:
            x = '0.'+x + '0'*(n-len(x)) + '*10^{}'.format(len(x))
        else:
            x = '0.'+ x[:n] + '*10^{}'.format(len(x))
    else:
        a,b = x.split('.')
        if float(a)==0 and pnot0 is not None: # 正数部分是0，则找小数部分第一个非零数在那里
            diff = pnot0 -point-1 # 第一个非零数和小数点中间有diff个0，对应-几次方
            b = b.lstrip('0')
            if len(b)>=n:
                x = '0.'+b[:n]+'*10^-{}'.format(diff)
            else:
                x = '0.'+ b+ '0'*(n-len(b))+'*10^-{}'.format(diff)
        else:
            if len(a)+len(b) < n:
                x = '0.'+a+b+ '0'*(n-len(a)-len(b)) + '*10^{}'.format(len(a))
            else:
                x = '0.' + (a+b)[:n] + '*10^{}'.format(len(a))

    xx.append(x)

if xx[0] == xx[1]:
    print('YES',xx[0])
elif xx[0].split('*')[0]== xx[1].split('*')[0]:
    print('YES', xx[0].split('*')[0]+'*10^0')
else:
    print('NO', xx[0],xx[1])

