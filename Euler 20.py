import math
string = str(math.factorial(100))
print(string)
total = 0
for i in string:
    total += eval(i)
