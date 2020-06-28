#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf-8 -*-



while 1:
    try:
        n = int(input())
        scoreList = list(map(int, input().strip().split()))
        if n<=0:
            print(0)
            continue
        result = [1]*len(scoreList)

        for i in range(n):
            if i-1>=0 and scoreList[i]>scoreList[i-1]:
                result[i] = result[i-1]+1

        for j in range(n,-1,-1):
            if j+1<n and scoreList[j]>scoreList[j+1]:
                result[j] = result[j+1]+1

        print(sum(result))

    except:
        break