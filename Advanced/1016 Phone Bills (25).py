#!/usr/bin/env.python
# -*- coding:utf-8 -*-
fee = input().split()
fee = [int(i) for i in fee]
# print(fee)
ffod = sum(fee)*60
N = int(input())

# {人:[（月，日，时，分，on或off），     ， ]}
olfl = {"on-line":0, "off-line":1} # 保证时间相同时on在off前面。这样在对时间序列排序时，可以把前序on, 同时间on, 同时间off给排除
d= {}
for i in range(N):
    name, time, line = input().split()
    time = [int(i) for i in time.split(":")]
    month = time[0]
    time.append(olfl[line])
    d.setdefault(name, []).append(time[1:])
# for k, v in d.items():
#     print(k, "\n", v)

Name = list(sorted(d.keys()))
'''
题意：It is guaranteed that at least one call is well paired in the input. 
竟然是指有on则一定有匹配的off，不是说每人至少有一次记录，可以全off。此时这个人的信息啥也不用输出。excuse me?
'''
def has_record(ll):
    i = 0
    while i<len(ll)-1:
        if ll[i][-1] < ll[i+1][-1]: # 有on在前off在后的情况则表示有通话记录
            return True
        i += 1
    return False

for name in Name:
    ll = d[name]
    ll.sort() # 对时间序列排序
    if not has_record(ll):
        continue
    print("{} {:0>2}".format(name, month))
    flag = 0
    on, off = None, None
    tft = 0
    for elem in ll:
        if elem[-1] == 0: # 动态规划匹配。若为on状态，则更新为最近一次on，flag标记1表示通话中
            flag = 1
            on = elem
        else:
            if flag == 1: # 碰到挂断，且flag标记为此前在通话，则形成一次有效通话
                flag = 0
                off = elem
                dd = off[0]-on[0]
                dh = off[1]-on[1]
                dm = off[2]-on[2]
                total = dd*1440+dh*60+dm
                # if total == 0: # on和off在同一个时间的情况，不形成有效匹配
                    # continue
                print('{:0>2}:{:0>2}:{:0>2} {:0>2}:{:0>2}:{:0>2} {} $'.format(*on[:-1],*off[:-1], total), end ='')
                if on[0] == off[0]: # 同一天
                    if on[1] == off[1]: # 同一小时
                        ft = dm*fee[on[1]]
                    else:
                        ft = (60-on[2])*fee[on[1]]
                        s = on[1] + 1 # 临时变量s记录进位后的数值
                        for x in range(s,off[1]):
                            ft += 60*fee[x]
                        ft += off[2]*fee[off[1]]
                else:
                    ft = (60-on[2])*fee[on[1]]
                    s = on[1]+1
                    for x in range(s,24):
                            ft += 60*fee[x]
                    s = on[0] + 1
                    for x in range(s, off[0]):
                        ft += ffod
                    for x in range(off[1]):
                        ft += 60 * fee[x]
                    ft += off[2] * fee[off[1]]
                print('{:.2f}'.format(ft/100))
                tft += ft
    if tft>0:
        print('Total amount: ${:.2f}'.format(tft/100))
