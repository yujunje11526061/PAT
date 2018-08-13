# 坑点在于输出控制以及输入有0多项式。
# 浮点数精度问题真是python一个大问题, 放弃

def haha():
    line1 = input().strip().split()
    line2 = input().strip().split()
    k1, line1 = int(line1[0]), line1[1:]
    k2, line2 = int(line2[0]), line2[1:]
    s = []
    k1 = len(line1)//2
    k2 = len(line2)//2
    while k1 > 0 and k2 > 0:
        if line1[0] == line2[0]:
            he = 0
            if abs(float(line1[1])) >= 0.05:
                he += float(line1[1])
            if abs(float(line2[1])) >= 0.05:
                he += float(line2[1])
            if abs(he) >= 0.05:
                s.extend([line1[0], '{:.1f}'.format(he)])
            k1 -= 1
            k2 -= 1
            line1 = line1[2:]
            line2 = line2[2:]
        elif line1[0] > line2[0]:
            if abs(float(line1[1])) >= 0.05:
                s.extend([line1[0], '{:.1f}'.format(float(line1[1]))])            
            k1 -= 1
            line1 = line1[2:]
        else:
            if abs(float(line2[1])) >= 0.05:
                s.extend([line2[0], '{:.1f}'.format(float(line2[1]))])
            k2 -= 1
            line2 = line2[2:]
    if k1 == 0 and k2 == 0:
        return s
    if k1 == 0:
        while k2 > 0:
            if abs(float(line2[1])) >= 0.05:
                s.extend([line2[0], '{:.1f}'.format(float(line2[1]))])
            k2 -= 1
            line2 = line2[2:]
        return s
    if k2 == 0:
        while k1 > 0:
            if abs(float(line1[1])) >= 0.05:
                s.extend([line1[0], '{:.1f}'.format(float(line1[1]))])
            k1 -= 1
            line1 = line1[2:]
        return s

s = haha()
if len(s) > 0:
    k = len(s)//2
    output = str(k) + ' ' + ' '.join(s)
    print(output)
else:
    print(0)
