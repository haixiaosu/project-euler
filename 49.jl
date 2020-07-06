import Primes

function get_digit_mask(n)
  mask = 0
  while n > 0
    mask |= 1 << (n % 10)
    n ÷= 10
  end
  mask
end

function main()
  primes = Primes.primes(1000, 9999)
  # We use a digit mask to determine what digits are used in the number.
  # Note that technically comparing digit masks is insufficient because the mask
  # does not tell you the number of times a d git is used. Thus, we (the human)
  # need to visually check the output to see if the numbers are permutations.
  # It turns out that this does not happen.
  digit_mask = [get_digit_mask(p) for p in primes]
  primes_set = Set(primes)
  for i in 1:length(primes)
    for j in i+1:length(primes)
      if digit_mask[i] != digit_mask[j]
        continue
      end
      diff = primes[j] - primes[i]
      next_prime = primes[j] + diff
      if in(next_prime, primes_set) && get_digit_mask(next_prime) == digit_mask[i]
        println(primes[i], " ", primes[j], " ", next_prime)
      end
    end
  end
end

main()
