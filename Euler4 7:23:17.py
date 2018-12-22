#Palindromic numbers
from math import *
def is_palindrome(x):
    #checks for palindromic nature
    #input number
    num = str(x)
    t = 0
    r = True
    while r:
        if t == int(len(num)/2):
            r = False
            return True
        if num[t]!=num[len(num)-t-1]:
            return False
        else:
            t += 1
q = []
for i in range(1,1000):
    for k in range(1,1000):
        q.append(i*k)
        
        
    
    
