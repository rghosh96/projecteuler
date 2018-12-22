import math
def factors(n):
    y = [x for x in range(1, math.ceil(math.sqrt(n)) + 1) if n % x == 0 and x != n]
    z = [int(n / x) for x in y[::-1] if x != math.sqrt(n)]
    g = y + z
    del g[len(g) - 1]
    return g
def d(n):
    t = 0
    for i in factors(n):
        t += i
    return t
q = []
for i in range(2,10001):
    temp = d(i)
    if temp != 1:
        if d(temp) == i:
            q.append([i, temp])
        
