def sieve(n):
    works = [True] * (n + 1)
    primes = []
    for a in range(2, n + 1):
        if works[a]:
            primes.append(a)
        for i in range(a + a, n + 1, a):
            works[i] = False
    return primes


def get_squares(n):
    res = set()
    for i in range(1, n // 2):
        if i * i > n:
            break
        res.add(i * i)

    return res



def main():
    MILLION = 1000000
    primes = sieve(MILLION)
    squares = get_squares(MILLION)
    prime_set = set(primes)

    for i in range(9, MILLION, 2):
        if i in prime_set:
            continue

        works = False
        for j in primes[1:]:
            if j >= i:
                break

            if ((i - j) // 2) in squares:
                works = True
                break

        if not works:
            print(i)
            break


if __name__ == "__main__":
    main()
