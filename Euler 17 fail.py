#counts letters
z = [str(x) for x in range(1001)]
a = len('thirty')
b = len('twenty')
c = len('forty')
d = len('fifty')
e = len('sixty')
f = len('seventy')
g = len('eighty')
h = len('ninety')
w = len('teen')
j = len('hundred')
k = len('one')
l = len('two')
m = len('three')
n = len('four')
o = len('five')
p = len('six')
q = len('seven')
r = len('eight')
s = len('nine')
t = len('ten')
total = 0
def v(i):
    global total
    if i[0] == '1':
        total += k
    elif i[0] == '2':
        total += l
    elif i[0] == '3':
        total += m
    elif i[0] == '4':
        total += n
    elif i[0] == '5':
        total += o
    elif i[0] == '6':
        total += p
    elif i[0] == '7':
        total += q
    elif i[0] == '8':
        total += r
    elif i[0] == '9':
        total += s
def ve(i):
    global total
    if i[1] == '1':
        total += k
    elif i[1] == '2':
        total += l
    elif i[1] == '3':
        total += m
    elif i[1] == '4':
        total += n
    elif i[1] == '5':
        total += o
    elif i[1] == '6':
        total += p
    elif i[1] == '7':
        total += q
    elif i[1] == '8':
        total += r
    elif i[1] == '9':
        total += s
def vef(i):
    global total
    if i[2] == '1':
        total += k
    elif i[2] == '2':
        total += l
    elif i[2] == '3':
        total += m
    elif i[2] == '4':
        total += n
    elif i[2] == '5':
        total += o
    elif i[2] == '6':
        total += p
    elif i[2] == '7':
        total += q
    elif i[2] == '8':
        total += r
    elif i[2] == '9':
        total += s
def ved(i):
    global total
    if i[1] == '1':
        vef(i)
        total += w
    elif i[1] == '2':
        vef(i)
        total += b
    elif i[1] == '3':
        vef(i)
        total += a
    elif i[1] == '4':
        vef(i)
        total += c
    elif i[1] == '5':
        vef(i)
        total += d
    elif i[1] == '6':
        vef(i)
        total += e
    elif i[1] == '7':
        vef(i)
        total += f
    elif i[1] == '8':
        vef(i)
        total += g
    elif i[1] == '9':
        vef(i)
        total += h


for i in z:
    if len(i) == 1:
        v(i)
    elif len(i) == 2:
        if i[0] == '1':
            if i[1] == '0':
                total += 3
            else:
                ve(i)
                total += w
        elif i[0] == '2':
            if i[1] == '0':
                total += b
            else:
                ve(i)
                total += b
        elif i[0] == '3':
            if i[1] == '0':
                total += a
            else:
                ve(i)
                total += a
        elif i[0] == '4':
            if i[1] == '0':
                total += c
            else:
                ve(i)
                total += c
        elif i[0] == '5':
            if i[1] == '0':
                total += d
            else:
                ve(i)
                total += d
        elif i[0] == '6':
            if i[1] == '0':
                total += e
            else:
                ve(i)
                total += e
        elif i[0] == '7':
            if i[1] == '0':
                total += f
            else:
                ve(i)
                total += f
        elif i[0] == '8':
            if i[1] == '0':
                total += g
            else:
                ve(i)
                total += g
        elif i[0] == '9':
            if i[1] == '0':
                total += h
            else:
                ve(i)
                total += h
    elif len(i) == 3:
        total += 3
        total += j
        v(i)
        ved(i)
de = k + l + m + n + o + p + q + r + s
fe = a + b + c + d + e + f + g + h + t
gen = (j * 9) + de
geno = (gen + 3) * 9 + fe

            
            
            












        
