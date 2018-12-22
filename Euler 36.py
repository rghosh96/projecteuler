#double base palindromes
a = []
ls = [str(x) for x in range(10, 10001)]
for k in ls:
    n = 0
    for i in range(len(k)):
        if n <= len(k) // 2:
            if k[n] == k[len(k) - n - 1]:
                n += 1
            else:
                continue
            if n == len(k) // 2 + 1:
                a.append(k)
b = []
c = []
for k in a:
    b.append(bin(eval(k)))
for k in b:
    c.append(k[2:])

