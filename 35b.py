def sieve(n):
    works = [True] * (n + 1)
    primes = []
    for a in range(2, n + 1):
        if works[a]:
            primes.append(a)
        for i in range(a + a, n + 1, a):
            works[i] = False
    return primes

def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return list(reversed(digits))


def make_num(digits):
    num = 0
    for d in digits:
        num *= 10
        num += d
    return num

def main():
    primes = sieve(1000000)
    primes_set = set(primes)
    res = []
    for p in primes:
        digits = get_digits(p)
        works = True
        for i in range(1, len(digits)):
            if make_num(digits[i:] + digits[:i]) not in primes_set:
                works = False
                break

        if works:
            res.append(p)

    print(len(res), res)


main()

