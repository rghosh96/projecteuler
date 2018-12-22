#fifth digit sums
lst = [str(x) for x in range(50)]
q = []
for i in lst:
    if len(i) >= 1:
        a = eval(i[0]) ** 5
        b,c,d,e = 0,0,0,0
    if len(i) >= 2:
        b = eval(i[1]) ** 5
        c,d,e = 0,0,0
    if len(i) >= 3:
        c = eval(i[2]) ** 5
        d,e = 0,0
    if len(i) >= 4:
        d = eval(i[3]) ** 5
        e = 0
    if len(i) >= 5:
        e = eval(i[4]) ** 5
        
    if a + b + c + d + e== eval(i):
        q.append(i)
p = []
for k in range(1000000):
    total = 0
    for i in str(k):
        total += eval(i)**5
    if total == k:
        p.append(k)
