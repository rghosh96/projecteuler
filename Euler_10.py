# This will be my solution for project Euler problem 10

# I am going to implement the sieve of Eratosthenes for the first time
# This will use a lot of memory up front and could probably be improved if need be

import time

def sieve(x):
    l = [x for x in range(3,x,2)]
    for i in l:
        k = list(filter(lambda x: x%i != 0 or x == i,l))
        if k == l:
            break
        else:
            l = k
    s = 0
    l.append(2)
    for i in l:
        s += i        
    return s

# That didn't work, tried several methods until I realized the issues and
# a better way to do it. There is an issue in recursively redefining the list
# that is being iterated over because the for loop generates a one time use
# iterator. This means any chages to the list will offset the index and skip
# entries. This issue is compounded over large input values

# I just realized something even smarter. Instead of removing the non prime
# numbers, I can just replace them with None! Also can iterate based on index


def sieve2(num):
    start = time.time()
    l = [x for x in range(1,num,2)]
    del l[0]
    n = 3
    k = 1
    while n < int(num**.5) + 1:
        k = 1
        while True:
            try:
                l[l.index(n) + k*n] = None
            except:
                IndexError
                break
            k += 1
        for i in l:
            try:
                if i > n:
                    n = i
                    break
            except:
                TypeError
                continue
    l.append(2)
    k = sum(filter(lambda x: x != None, l))
    print(time.time() - start)
    return k
# This worked for sieve2(2e6) in 2.1s
# Not the fastest solution, but I'm proud of myself for the new implementation

# Here is the standard code for creating a generator as an iterator.

class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()

# This is the same thing as a generator implementation

# Note: the following also produces a generator:
# (x for x in range(12)) for example
# Thus, a list comprehension is essentially passing a generator to the list function
def firstn_1(n):
    num = 0
    while num < n:
        yield num
        num += 1


# Here is what seems to be the most clever sieve I've found
# Though it also seems it could be implemented better...
# This is essentially the same thing that I did, just more compact and clever
# due to the c**2 range start point.

def PrimeSumPro(n):
    "Returns sum of primes less than n"
    primes=[1]*n
    primes[0],primes[1],h = 0,0,[]
    c =2
    while int(c**2) <= n:
        if primes[c] == 1:
            #This is the kicker. It works because primes[2] corresponds to 3.
            for a in range(c**2,n,c):
                primes[a]=0
        c+=1
    for p,q in enumerate(primes):        
        if (q==1):
            h.append(p)
    return sum(h)
