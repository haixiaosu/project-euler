using Combinatorics
using Primes

function isPrime(x, primes)
  for p in primes
    if x % p == 0
      return false
    end
  end
  return true
end

function main()
  primes = Primes.primes(10^5)
  max_x = 0
  for n in 1:9
    for x in Combinatorics.permutations(1:n)
      x = foldl((a, b) -> 10 * a + b, x; init=0)
      if isPrime(x, primes) && x > max_x
        max_x = x
      end
    end
  end
  println(max_x)
end

main()
