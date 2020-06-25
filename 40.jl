function get_digit(d)
  digit_count = 0
  # Figure out if digit `d` is part of the numbers that have `k` digits.
  k = 1
  while k < 10
    delta = 9 * 10^(k - 1) * k
    if digit_count + delta >= d
      break
    end
    digit_count += delta
    k += 1
  end

  d -= digit_count + 1
  # Find the number which contains digit `d`.
  num = (d ÷ k) + 10^(k - 1)
  # We want `k - (d % k)`th digit of `num`.
  return (num ÷ 10^(k - (d % k) - 1)) % 10
end

function main()
  prod(get_digit.(10 .^ (0:6)))
end

@time res = main()
println(res)
