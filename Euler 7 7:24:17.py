#finds nth prime number

global is_prime

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    r = True
    t = 4
    while r:
        if x % t == 0:
            return False
        if t >= int(x/2):
            return True
        t += 1

def prime(n):
    #returns nth prime
    temp = 0
    num = 2
    count = 0
    while count < n:
        if is_prime(num):
            count += 1
            temp = num
        num += 1
    return temp
        
        
