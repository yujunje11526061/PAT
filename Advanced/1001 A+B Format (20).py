si = input().split()
a, b  = map(int, si)
sum_ = a + b
ssum = str(sum_)
if sum_ == 0:
    print(sum_)
elif sum_ > 0:
    n  = len(ssum)
    d = n//3
    docker = []
    for i in range(d):
        docker.append(ssum[-3:])
        ssum = ssum[:-3]
    if len(ssum) != 0:
        docker.append(ssum)
    docker.reverse()
    output = ','.join(docker)
    print(output)
else:
    ssum = ssum[1:]
    n  = len(ssum)
    d = n//3
    docker = []
    for i in range(d):
        docker.append(ssum[-3:])
        ssum = ssum[:-3]
    if len(ssum) != 0:
        docker.append(ssum)
    docker.reverse()
    output = '-' + ','.join(docker)
    print(output)


    
        
    
