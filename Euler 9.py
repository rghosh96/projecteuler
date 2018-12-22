# This will be my solution for project Euler problem 9
# This will find the pythagorean triplet for which the sum is 1000
global generate_values
def generate_values(number):
    l = []
    for i in range(1,number-1):
        for k in range(1,number - i):
            l.append((i,k, number- i - k))
    return l
def find_triplet(number):
    a,b,c = 0,0,0
    l = generate_values(number)
    for i in l:
        if i[0]**2 + i[1]**2 == i[2]**2:
            a,b,c = i[0],i[1],i[2]
        else:
            pass
    return a*b*c
