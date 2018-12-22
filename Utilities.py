# This will be my own personal utilities file of good tools I've built

# This is a tokenizer to return a tokenized list of numbers from a string input
# Probably could be better but I like it.

def tokenizer(x):
    from queue import deque
    x = str(x)
    left = deque([])
    tokens = []
    count = 0
    while count < len(x)+1:
        temp = ''
        if count < len(x) and x[count].isdigit():
            left.append(x[count])
        else:
            while True:
                try:
                    temp += left.popleft()
                except:
                    IndexError
                    break
            try:
                int(temp)
                tokens.append(int(temp))
            except:
                ValueError
                pass
        count += 1
    return tokens

# This is the standard Euclidean algorithm.

def gcd(a,b):
    "Return the gcd of a and b"
    if b > a:
        a,b = b,a
    while b != 0:
        t = b
        b = a%b
        a = t
    return a

# This is a lazy prime factorization sieve. I'll do the quadratic sieve later.

def lazy_sieve(n):
    "yields prime factors of n"
    x = 2
    while n > 1:
        if n%x == 0:
            yield x
            n = n/x
            x = 2
        else:
            x += 1

def sieve():
    yield from (2,3,5,7) # Without these, the algorithm chases and gives Error
    from itertools import chain, accumulate, cycle, count, islice # Tools for our generator
    wheel = [4,2,4,2,4,6,2,6] # Our pattern of numbers to include as candidates, starting at 7, i.e. 7+4=11, 11+2=13, etc.
    wheeled = islice(accumulate(chain([7], cycle(wheel))), 1, None) # Our candidate generator 7,11,13,17,19,....
    ps = sieve() # One instance of the entire generator function to call later when we want to advance the Sieve
    D = {} # Dictionary to store our predictions of candidates which are multiples of primes
    count = 0 # This is due to our need to start the wheel in the next position when we advance the sieve
    next(ps),next(ps),next(ps),next(ps) # getting 2,3,5,7 out of the way
    p = 7 # Starting Sieve of Eratosthenes at p=7
    psq = p**2 # We run the first round until psq=49
    for i in wheeled: # Our candidate generator
        if i in D: # Our predicted composites
            step = D[i][2] # We have to store the step based on where we are in cycle(wheel)
                            # because our new key will be the current key + step, i.e. 49+28=77
        elif i < psq: # If it is not a predicted composite, it is prime.
            yield i
            continue # We do not want to change our dictionary keys so we proceed to the next i in wheeled
        else: # Othewise, we have found all the primes less than psq, so we need to advance the sieve to the next prime
              # i.e. p=7, i=psq=49, now we need p=11 and psq=121 and we will continue our sieve
            assert i == psq
            k = islice(cycle(wheel),count,None) # Creates a new generator for our position in the wheel. Each prime
            # needs its own unique position. i.e. 121+11*4 is wrong. We need to start 11 at the 2nd position
            # in wheeled, 2, so that 121+11*2=143, otherwise we would include 143 in our results. 143=11*13, not prime.
            step = p*next(k) # The distance to our predicted composite multiple, i.e. 11*2=22
            D[i] = k,p,step # Creating new dictionary entry for multiples of p. i.e. {49:k,7,28} includes unique generator k
            p = next(ps) # Advancing our sieve to the next prime, i.e. p=next(ps)=11.
            # Note calling ps does NOT cause recursion because p is one instance of sieve() and already has found
            # the next prime number, i.e. 11, which was found on our 2nd iteration of i in wheeled.
            psq = p**2 # Redefining psq i.e. 121
            count += 1 # Advancing our slice point in the next instance of k i.e. 4 for psq=169
        D[i+step] = D[i][0],D[i][1], next(D[i][0])*D[i][1] # Updating our dictionary
        D.pop(i) # removing the old key because it is no longer needed. i.e. D[i+step]=D[77], we don't need D[49] anymore.
        # This is a very important step and the efficiency of the algorithm owes a lot to this idea
def primes(n):
    "returns list of primes less than n"
    l = []
    a = sieve()
    t = 0
    while t < n:
        t = next(a)
        l.append(t)
    l.pop()
    return l

def first_primes(n):
    "returns list of first n primes"
    a = sieve()
    l = [next(a) for x in range(n)]
    return l

def powerset(iterable):
    from itertools import chain, combinations
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
