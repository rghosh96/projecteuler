file = open('names.txt', 'r+')
string = str(file.read())
ls = string.split(',')
y = []
for i in ls:
    y.append(i.strip('"'))
y.sort()
alpha = 'abcdefghijklmnopqrstuvwxyz'.upper()
b = []
for i in y:
    total = 0
    for k in i:
        total += (alpha.index(k) + 1)
    b.append(total)
a = []
k = 1
for i in b:
    temp = i * k
    a.append(temp)
    k += 1
to = 0
for i in a:
    to += i
