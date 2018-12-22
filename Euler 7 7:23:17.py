#attempt at aks primality test

#(x-1)^p - (x^p - 1)
from math import *

global ch
global b
global aks

def ch(n,r):
    return int(factorial(n)/(factorial(r)*factorial(n-r)))
def bi(p):
    q = []
    for i in range(1,p):
        q.append(ch(p,i))
    return q
def aks(x):
    return
