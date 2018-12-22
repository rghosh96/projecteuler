def fib(n):
    a = 1
    b = 1
    ls = []
    for i in range(n):
        a, b = b, a + b
        ls.append(a)
    return ls
