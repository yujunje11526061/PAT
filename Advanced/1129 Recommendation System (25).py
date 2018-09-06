#!/usr/bin/env.python
# -*- coding:utf-8 -*-
# n, k = map(int, input().split())
# seq = map(int, input().split())
# start = next(seq)
# l = [0] * 500001
# l[start] = 1
# recset = {start}
# rec = [start]
# if k == 0:
#     pass
# else:
#     for i in range(n - 1):
#         item = next(seq)
#         print('{}: '.format(item), end='')
#         print(*rec)
#         l[item] += 1
#         if item in recset:
#             rec.sort(key=lambda x: (-l[x], x))
#         else:
#             if len(rec) < k:
#                 recset.add(item)
#                 rec.append(item)
#                 rec.sort(key=lambda x: (-l[x], x))
#             else:
#                 if (l[item], -item) > (l[rec[-1]], -rec[-1]):
#                     recset.remove(rec[-1])
#                     recset.add(item)
#                     rec[-1] = item
#
#

def main():
    line = input().split(" ")
    n = int(line[0])
    k = int(line[1])
    line = input().split(" ")
    for i in range(1, n):
        temp = line[:i]
        temp = sorted(temp, key=lambda x: (-temp.count(x), int(x)))
        result = [temp[0]]
        count = k
        for j in range(1, i):
            try:
                if temp[j] != temp[j - 1]:
                    result.append(temp[j])
                    count -= 1
                if count == 1:
                    break
            except:
                pass
        result = [x for x in result]
        print(line[i], ':', ' ', ' '.join(result), sep='')


if __name__ == "__main__":
    main()
