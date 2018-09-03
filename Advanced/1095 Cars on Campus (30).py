#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
1. 此类化成最小计时单位来算，两个化成秒的函数熟练编写
2. 记录按时间顺序排列，按时间非递减的，从头扫描模拟
3. count数组和record数组维度一致，对应记录每个record发生时停着的车辆，也是按时间非递减的
4. in和out就近匹配。连续两个in按后面的，要把前面那个in导致的一系列计数都扣掉(-1)，本次当作全新的in来算
5. 连续两个out按前面的，取前一record的记录，表明此记录是废记录，对计数无影响。
6. 防止count[-1]空数组时越界，用try...except，获得原谅比取得同意更省事
7. 同一时刻可能同时有多个进出，二分查询的时候找同时间最后的记录。。
'''
from collections import defaultdict
def to_s(hms:str):
    hh,mm,ss = map(int,hms.split(':'))
    return hh*3600+mm*60+ss
def to_hms(ts:int):
    hh,ts = divmod(ts, 3600)
    mm, ss = divmod(ts,60)
    return "{:0>2}:{:0>2}:{:0>2}".format(hh,mm,ss)

N, K = map(int, input().split())
record = []
for i in range(N):
    r =input().split()
    r[1] = to_s(r[1])
    record.append(r)

record.sort(key = lambda x:x[1])

maxt = 0
maxtcar = []
in_or_out = defaultdict(lambda :'out')
parking_time = defaultdict(lambda: 0)
time_in = {}
count = []
for i in range(N):
     # 车牌，时间，出入
    plate, t, io = record[i]
    if in_or_out[plate] != io:
        if io == 'in':
            in_or_out[plate] = 'in'
            time_in[plate] = t
            try:
                count.append(count[-1]+1)
            except IndexError:
                count.append(1)
        else:
            in_or_out[plate] = 'out'
            parking_time[plate] += t - time_in[plate]
            count.append(count[-1]-1)
            if parking_time[plate] > maxt:
                maxt = parking_time[plate]
                maxtcar = [plate]
            elif parking_time[plate] == maxt:
                maxtcar.append(plate)
    else:
        if io == 'in':
            time_in[plate] = t # 连续两个in，则按后面的为准。并修改前面的记录
            p =i-1
            while record[p][0] != plate:
                count[p] -= 1
                p -= 1
            count[p] -= 1
            count.append(count[-1]+1)
        else:
            try:
                count.append(count[-1])
            except IndexError:
                count.append(0)

def calculate(s,e):
    if query<record[0][1]:
        return 0
    head,tail = s,e
    while head<=tail:
        mid = (head+tail)//2
        ct = record[mid][1]
        if query >= ct:
            head = mid+1
        else:
            tail = mid-1
    # 取不到结束时head < query < tail
    # 取到结束时tail == query < head
    return tail

last_query = 0
for _ in range(K):
    query = to_s(input())
    last_query = calculate(last_query,N-1)
    print(count[last_query])
maxtcar.sort()
print(*maxtcar, to_hms(maxt))

