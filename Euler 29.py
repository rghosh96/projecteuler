a = []
for k in range(2, 101):
    for i in range(2, 101):
        if k ** i not in a:
            a.append(k ** i)
