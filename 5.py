primes = [2,3,5,7,11,13,17,19]
facts = [1] * len(primes)
for i in range(2, 21):
    for j, p in enumerate(primes):
        c = 1
        while i > 1 and i % p == 0:
            i //= p
            c *= p
        facts[j] = max(facts[j], c)
prod = 1
for f in facts:
    prod *= f
print(prod)
    