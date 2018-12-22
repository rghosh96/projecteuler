a = []
import math
for i in range(1000000):
    y = str(i)
    h = 0
    count = 0
    for g in range(math.floor(len(y)/2)):
        if y[h] == y[len(y)-1-h]:
            h += 1
            count += 1
            if count == math.floor(len(y)/2):
                a.append(i)
            else:
                pass
        else:
            break
t = []
for i in a:
    if len(str(i)) >= 5:
        for y in range(100,1000):
                if i % y == 0:
                    if len(str(int(i / y))) == 3:
                        t.append(i)
                    else:
                        pass
                else:
                    pass
print(t)
                
