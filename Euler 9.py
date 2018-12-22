#special pythonagorean triplet
import math
l = []
t = []
for i in range(1000):
    for h in range(1000):
        c = math.sqrt(i**2 + h**2)
        if c % 1 == 0:
            l.append([i, h, c])
for i in l:
    if i[0] + i[1] + i[2] == 1000:
        t.append(i)
