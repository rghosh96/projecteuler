#find lonest collatz sequence with first term < 1 million
def c(x):
    f = x
    t = [x]
    while f > 1:
        if f % 2 == 0:
            f = f / 2
        elif f % 2 != 0:
            f = 3 * f + 1
        t.append(f)
    return t
a = 0
q = 1
for i in range(1000000):
    if len(c(q)) > a:
        a = len(c(q))
        h = q
    q += 1
    
    
