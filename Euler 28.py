ls = [1]
total = 3
check = 0
n = 2
k = 1
while k < 1001:
    ls.append(total)
    check += 1
    if check == 4:
        check = 0
        n += 2
        k += 2
    total += n

    
