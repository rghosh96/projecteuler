#Euler 14
# Longest Collatz sequence for s0 less than 1 million

def collatz(n):
    l = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
            l.append(n)
        else:
            n = 3*n + 1
            l.append(n)
    return l
current = 0,0
for i in [x for x in range(1000000)][500000:-2]:
    if len(collatz(i)) > current[0]:
        current = len(collatz(i)),i
print(current[1])
    
