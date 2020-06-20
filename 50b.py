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
    MILLION = 1000000
    primes = sieve(MILLION)
    prime_set = set(primes)

    max_len = 0
    best_prime = 0
    for i in range(len(primes)):
        cur_sum = primes[i]
        for j in range(i + 1, len(primes)):
            cur_sum += primes[j]
            if cur_sum in prime_set:
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    best_prime = cur_sum

            if cur_sum > primes[-1]:
                break
    print(max_len, best_prime)


if __name__ == "__main__":
    main()
