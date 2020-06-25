using Combinatorics
using Primes

function main()
  primes = Primes.primes(18)
  make_num(x) = foldl((a, b) -> 10 * a + b, x; init=0)
  nums = []
  for x in Combinatorics.permutations(0:9)
    works = true
    for (i, p) in enumerate(primes)
      if make_num(x[(i + 1):(i + 3)]) % p != 0
        works = false
        break
      end
    end

    if works
      push!(nums, make_num(x))
    end
  end
  println(sum(nums))
end

main()
