def factorize(number):
    prime = 0
    i = 2
    while i < number:
        while number % i == 0:
            number = number / i
        prime = number
        i += 1
    return prime

print(factorize(600851475143))
