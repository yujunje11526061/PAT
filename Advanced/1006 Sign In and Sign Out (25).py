#!/usr/bin/env.python
# -*- coding:utf-8 -*-
M = int(input())
docker = []
for i in range(M):
    id, st, et = input().split()
    st = int(''.join(st.split(':')))
    et = int(''.join(et.split(':')))
    docker.append((id, st, et))

mi, ma = docker[0][1], docker[0][2]
idmi, idma = docker[0][0], docker[0][0]
for id_, s, e in docker[1:]:
    if s < mi:
        mi = s
        idmi = id_
    if e > ma:
        ma = e
        idma = id_

# idmi = min(docker, key = lambda x:x[1])[0]
# idma = max(docker, key = lambda x:x[2])[0]
print(idmi, idma)