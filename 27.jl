using Primes

function main()
  primes = Primes.primes(1000)
  prime_set = Set(Primes.primes(1000000))

  max_n = 1
  max_a = 1
  max_b = 1
  for b in primes
    for b2 in primes
      a = b2 - b - 1
      n = 2
      while true
        n += 1
        p = n^2 + a * n + b
        if !in(p, prime_set)
          break
        end
      end

      if n - 1 > max_n
        max_a = a
        max_b = b
        max_n = n - 1
      end
    end
  end
  println(max_a * max_b, " ", max_a, " ", max_b)
end


main()
