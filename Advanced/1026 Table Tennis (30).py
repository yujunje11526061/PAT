#!/usr/bin/env.python
# -*- coding:utf-8 -*-
'''
巨坑连连：
（1）每个乒乓球台的服务时间在8：00~21：00之间，超过21：00的不再服务
（2）等待队列中，VIP的优先级体现在当有空VIP专用球台时，VIP客户可以直接使用，而不管前面是否有普通客户在等待
（3）最为重要的一点，当有普通球台和VIP球台时，VIP客户遵循选择最小编号的VIP球台（VIP就要这么任性），而非编号最小的球台；普通客户遵循选择最小的球台
（4）每个人的服务时间在2小时之内，超过2小时的按2小时处理；
（5）注意最后计算等待时间时采用的是四舍五入，此题可以取余数和30比较
'''
import heapq as hq
from collections import deque
import decimal

N = int(input())
start = 8 * 3600
end = 21 * 3600


def change_time(s: str):
    s = s.split(':')
    t = int(s[0]) * 3600 + int(s[1]) * 60 + int(s[2])
    return t


def change_time_rev(t: int):
    HH, t = divmod(t, 3600)
    MM, SS = divmod(t, 60)
    return '{:0>2}:{:0>2}:{:0>2}'.format(HH, MM, SS)

line = []
vip_served = {}  # 记录有哪些VIP以及是否被服务
serve_time = {}
for i in range(N):
    ss = input().strip().split()
    arrive, dt, vip = change_time(ss[0]), int(ss[1])*60, int(ss[2])
    if dt > 7200:
        dt = 7200
    line.append([arrive, dt])
    if vip:
        vip_served[arrive] = False

line.sort()
line = deque(line)
K, M = map(int, input().split())
all_table = [[start, i] for i in range(K)]
vip_table = map(int, input().split())
vt = [False] * K
serve_count = [0] * K
for i in vip_table:
    vt[i - 1] = True

while len(line) > 0:
    if line[0][0] >= end:
        break

    first = line[0]
    while all_table[0][0] < first[0]:  # 把空闲时间<队首人arrive的变成arrive后再放回桌队里
        head = hq.heappop(all_table)
        head[0] = first[0]
        hq.heappush(all_table, head)

    table = hq.heappop(all_table)
    if table[0]>=end:
        break
    pair = None

    if vt[table[1]] and len(line) > 0:  # 如果空出的是VIP桌，看是否有VIP在等
        for i in range(len(line)):
            if vip_served.get(line[i][0]) is False and line[i][0]<=table[0]: # 有VIP在等
                pair = line[i]
                line.remove(pair)
                vip_served[pair[0]] = True
                break
        if pair is None: # 无VIP在等，则普通人占用VIP桌
            pair = line.popleft()
    elif vip_served.get(first[0]) == False:  # 不是VIP桌，但人是未服务的VIP，则要考虑弹出普通桌时有没有同时空出的但是编号更大的VIP桌，这些桌子因为编号问题在后面
        if not vt[table[1]]:
            stack = []
            while len(all_table) > 0 and all_table[0][0] == table[0]:
                if vt[all_table[0][1]]:  # 下一个是同时间的VIP桌，则用VIP桌，把非VIP桌的放回去
                    stack.append(table)
                    table = hq.heappop(all_table)
                    break
                else:  # 下一个是同时间的普通桌，则先用容器暂存，继续往后扫描
                    stack.append(hq.heappop(all_table))
            for table_ in stack:
                hq.heappush(all_table, table_)
        pair = line.popleft()
        vip_served[pair[0]] = True
    else:  # 空出的是普通桌，人是普通人，以及VIP到来时没空VIP桌，全部正常进行
        pair = line.popleft()
        if vip_served.get(pair[0]) == False:
            vip_served[pair[0]] = True

    arrive, dt = pair
    serve_count[table[1]] += 1
    serve_time[arrive] = table[0]
    table[0] += dt
    hq.heappush(all_table, table)

ll = []
for arrive, serve in serve_time.items():
    if serve < end:
        ll.append([serve, arrive, serve - arrive])

ll.sort()
for serve, arrive, wait in ll:
    serve = change_time_rev(serve)
    arrive = change_time_rev(arrive)
    wait, left = divmod(wait, 60)  # python 的四舍五入真坑
    if left>=30:
        wait += 1
    print(arrive, serve, wait)

print(*serve_count)
