
import math

def get_primes(n):
    works = [True] * (n + 1)
    primes = []
    for a in range(2, n + 1):
        if works[a]:
            primes.append(a)
        for i in range(a + a, n + 1, a):
            works[i] = False
    return primes
    
def factorize(n, primes):
    factorization = []
    for i, p in enumerate(primes):
        if p > n: break
        num = 0
        while n % p == 0:
            n /= p
            num += 1
        if num > 0:
            factorization.append((p, num))
    return factorization

def generate_totient(n):
    totient_mem = [1] * (n + 1)
    primes = get_primes(math.floor(math.sqrt(n)))
    result = [0]  # Totient(0) = 0
    for i in range(1, n + 1):
        result.append(totient_faster_hopefully(i, primes, totient_mem))
    return result

def totient_faster_hopefully(n, primes, totient_mem):
    result = 0
    for p in primes:
        if p >= n:
            result = p - 1
            break
        a = 1
        y = n
        while y % p == 0:
            y //= p
            a *= p
        if a > 1:
            if a != n:
                result = totient_mem[y] * totient_mem[a]
            else:
                result = a//p * (p - 1)
            break
    if result == 0:
        result = n - 1
    totient_mem[n] = result
    return result
    
def is_permutation(x, y):
    counts = [0] * 10
    while x > 0:
        digit = x % 10
        counts[digit] += 1
        x //= 10
    while y > 0:
        digit = y % 10
        counts[digit] -= 1
        y //= 10
    for c in counts:
        if c != 0:
            return False
    return True
    
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def is_palindrome(x):
    x_string = str(x)
    length = len(x_string)
    if length %2 == 1:
        return False
    first_half = x_string[:length/2]
    second_half = x_string[length/2:]
    return first_half[::-1] == second_half
