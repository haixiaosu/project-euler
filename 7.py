import math
primes = [] # Forget about 2
x = 3
while len(primes) < 10000:
    works = True
    max_fact = math.floor(math.sqrt(x))
    for p in primes:
        if p > max_fact:
            break
        if x % p == 0:
            works = False
            break
    if works:
        primes.append(x)
    x += 2
print(primes[-1])