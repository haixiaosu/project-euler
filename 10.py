import math
isprime = [True] * 2000001
primesum = 0
for i in range(2, len(isprime)):
    if not isprime[i]:
        continue
    primesum += i
    for j in range(i + i, len(isprime), i):
        isprime[j] = False
print(primesum)