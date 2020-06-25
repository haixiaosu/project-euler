using Primes

function gen_possible(max_pow)
  # Pre-compute number of possible numbers in range
  # 1:100, 2:200, 3:300 ... max_pow:max_pow*100
  num_possible = []
  nums = Set{Int32}()
  for i = 1:max_pow
    nums = union(nums, Set(i:i:100*i))
    push!(num_possible, length(nums))
  end
  return num_possible
end

function main()
  base_num_dict = Dict{Int32, Int32}()
  for i = 2:100
    factors = Primes.factor(i)
    pow_gcd = gcd(values(factors)...)
    base_num = 1
    for (prime, power) in factors
      base_num *= prime^(power ÷ pow_gcd)
    end
    if !haskey(base_num_dict, base_num)
      base_num_dict[base_num] = pow_gcd
    else
      base_num_dict[base_num] = max(base_num_dict[base_num], pow_gcd)
    end
  end

  num_possible = gen_possible(6)

  total = 0
  for (base, max_pow) in base_num_dict
    # Subtract one because exponent cannot be 1.
    total += num_possible[max_pow] - 1
  end
  println(total)
end

main()
