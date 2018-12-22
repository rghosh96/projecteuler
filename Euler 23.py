#sum of all positive integers that are not the sum of two abundant numbers
import math
def div(k):
    temp = []
    ls = []
    for i in range(1, math.ceil(math.sqrt(k)) + 1):
        if k % i == 0:
            temp.append(i)
    for i in temp:
        ls.append(i)
        a = int(k / i)
        if a not in temp:
            ls.append(a)
    ls.sort()
    ls.remove(k)
    return ls
def num(z):
    y = div(z)
    total = 0
    for i in y:
        total += i
    if total > z:
        return z
def gen(n):
    ls = []
    for i in range(1, n + 1):
        if num(i) != None:
            ls.append(num(i))
    return ls
def ab(n):
    ls = []
    a = []
    for i in range(24, n + 1):
        for k in gen(i):
            if i - k in gen(i):
                ls.append(i)
    for i in range(24, ls[len(ls) - 1]):
        if i not in ls:
            a.append(i)
    return a
def odd(n):
    b = []
    for i in range(24, n):
        if i % 2 != 0:
            b.append(i)
    return b
            
        
        
        
