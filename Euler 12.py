#first triangle number to have over 500 factors
t = []
import math
def gen(x):
    global t
    for i in range(x + 1):
        a = 0
        for k in range(i + 1):
            a += k
        t.append(a)
    t.remove(0)
    return t
def g(x):
    global t
    for i in range(x + 1):
        a = 0
        for k in range(i + 1):
            a += k
        t.append(a)
    t.remove(0)
    count = 0
    for i in t:
        if i > 1000:
            for b in range(1, math.ceil(math.sqrt(i))):
                if i % b == 0:
                    count += 1
                if count == 250:
                    return i
            else:
                count = 0
            
        
