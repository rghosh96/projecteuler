#pandigital sums
import math
def f(n):
    temp = []
    temp1 = []
    for k in range(1, math.ceil(math.sqrt(n))):
        if n % k == 0:
            temp.append(k)
    for k in temp:
        temp1.append(k)
        temp1.append(n // k)
    if math.sqrt(n) % 1 == 0:
        temp1.append(int(math.sqrt(n)))
        temp1.append(int(math.sqrt(n)))
    temp1.sort()
    return temp1
def pair(x):
    n = 0
    ret = []
    for k in x[:len(x) // 2]:
        ret.append([x[n], x[len(x) - 1 - n]])
        n += 1
    return ret
ans = []
temp = []
for i in range(100000):
    h = pair(f(i))
    for t in h:
        for b in t:
            t[t.index(b)] = str(b)
        h[h.index(t)] = ''.join(t)
    for k in h:
        if '1' in k or '1' in str(i):
            if '2' in k or '2' in str(i):
                if '3' in k or '3' in str(i):
                    if '4' in k or '4' in str(i):
                        if '5' in k or '5' in str(i):
                            if '6' in k or '6' in str(i):
                                if '7' in k or '7' in str(i):
                                    if '8' in k or '8' in str(i):
                                        if '9' in k or '9' in str(i):
                                            temp.append([k, str(i)])
    
        
            
