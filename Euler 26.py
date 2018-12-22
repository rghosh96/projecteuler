from decimal import *
getcontext().prec = 10000
ls = []
#prime generator
import math
t = []
def prime(n):
    global t
    t.append(2)
    t.append(3)
    for num in range(n):
        if num % 2 == 0:
            continue
        y = math.ceil(math.sqrt(num))
        for i in range(3,y + 2,2):
            if num % i != 0:
                pass
            else:
                break
        else: t.append(num)
    t.remove(1)

for i in range(2, 1000):
    a = Decimal(1)
    ls.append(str(a / Decimal(i)))
count = 0
pop = []
for i in ls:
    for k in range(1, len(i)):
        p = i[:k]
        if p in i[i.index(p) + len(p):]:
            continue
        else:
            pop.append(count)
            break
        count += 1
    else:
        count += 1
temp = []
for i in ls:
    f = i.lstrip('0')
    temp.append(f.lstrip('.'))
total = ''
total1 = ''
for y in temp:
    output = ''
    b = []
    for q in range(1, 20):
        for i in range(q + 1, len(y)):
 s           if i == 1:
                continue
            if y[q:i] == y[i:(i*2 - q)]:
                output = y[q:i]
                b.append(output)
                break
            else:
                pass
        le = 0
        for i in b:
            if len(i) > le:
                le = len(i)
                output = i
    if len(output) > len(total):
        total = output
for i in temp:
    if total in i:
        print(temp.index(i))
        break
