#factorial digit sums
import math
ls = [str(x) for x in range(3, 10000000)]
a = []
for k in ls:
    total = 0
    for i in k:
        total += math.factorial(eval(i))
    if total == eval(k):
        a.append(k)
