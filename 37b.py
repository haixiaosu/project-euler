def sieve(n):
    works = [True] * (n + 1)
    primes = []
    for a in range(2, n + 1):
        if works[a]:
            primes.append(a)
        for i in range(a + a, n + 1, a):
            works[i] = False
    return primes


def main():
    primes = sieve(1000000)
    primes_set = set(primes)
    primes_set.add(0)
    res = []
    for p in primes[4:]:
        works = True

        tmp = p
        digits = 0
        while tmp > 0:
            tmp //= 10
            digits += 1
            if tmp not in primes_set:
                works = False
                break

        if not works:
            continue

        tmp = p
        while digits > 0:
            tmp = tmp % (10**digits)
            digits -= 1
            if tmp not in primes_set:
                works = False
                break

        if works:
            res.append(p)

    print(sum(res), res)


main()
