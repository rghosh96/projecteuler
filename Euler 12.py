# This will be my solution to project Euler problem 12.
# We are to find the first triangular number with over 500 divisors

# I am going to use a generator to save memory and to practice their usage
# This was garbage. The formula is literally .5(n)(n+1)....
"""
def triangles(n):
    #generates nth triangle number
    ans = 0
    for i in range(0,n):
        ans += i
        yield ans
"""
# I am going to do messy code here and use my sieve from problem 10 to generate
# n primes so that I can check divisibility quickly

from Utilities import sieve, first_primes, primes, powerset
import math

# Factors any integer using sieve prime generation and reursive wheel division
# This took entirely too long to write correctly
# This is garbage
"""
def factor(x):
    "Returns factors of x"
    h = PrimeSumPro(x)
    factors = []
    ans = [x]
    k = x
    while k > 1:
        for i in h:
            if k%i == 0:
                factors.append(i)
                # This is the reduction step
                k = k/i
                ans.append(int(k))
            else:
                continue
    temp = [x for x in factors if x not in ans]
    temp += ans
    for i in temp:
        if int(x/i) not in temp:
            temp.append(int(x/i))
    return temp
def triangle(n):
    #Returns first triangular number with greater than n factors
    count = 0
    count1 = 3
    while count <= n:
        k = next(triangles(count1))
        if len(factor(k)) > count:
            count = len(factor(k))
        else:
            pass
        count1 += 1
    return count1
"""

# This will be a triangle number generator

def triangle(n):
    "Returns nth triangular number"
    return int(.5*n*(n+1))
def ans(n):
    "Returns prime factorization of n"
    prime_factors = primes(math.ceil(math.sqrt(n)))
    l = []
    while 1:
        for i in prime_factors:
            if n%i == 0:
                n = n/i
                l.append(i)
                break
        else:
            l.append(int(n))
            break
    if 1 in l:
        l.pop()
    return l

def factors(n):
    "Returns set of factors of n"
    l = powerset(ans(n))
    next(l)
    a = []
    a.append(1)
    for i in l:
        temp = 1
        for k in i:
            temp *= k
        a.append(temp)
    return set(a)

def numf(n):
    "Returns number of factors of n"
    return len(factors(n))
# This was not an accurate algorithm lol
# Just going to go ahead and solve the problem the normal way

def smallest(n):
    "Returns smallest number with at least n factors"
    primes = []
    primef = []
    a = sieve()
    num = 1
    while num < n:
        temp = next(a)
        num *= 2
        primes.append(temp)
        primef.append(0)
    print(primes)
    num = 1
    answer =  1
    while num < n:
        for index,i in enumerate(primes):
            if index == len(primes)-1:
                break
            while i*(primef[index]) < primes[index+1]:
                num = num/(primef[index]+1)
                primef[index] += 1
                num *= (primef[index]+1)
                answer *= i
            if index < primef.index(0)-1:
                continue
            else:
                num *= 2
                answer *= primes[primef.index(0)]
                primef[primef.index(0)] += 1
                break
    print(primef)
    return answer
def smallest_triangle(n):
    count = 11167
    while 1:
        if numf(triangle(count)) > n:
            print(count)
            return triangle(count)
        else:
            count += 1
# This could have been improved by actually writing an algorithm to find the
# smallest number with n factors and starting from the n value right beneath
# that after solving that quadratic equation.
# That would've been very fast.
# The way to do that, for future reference, is for 500 as an example, to
# generate all partitions of ceil(log2(500)), which is 9, and map them
# to the first 9 primes. Whichever is smallest wins.
# This is only doable because the partition of 9 is so small.
















