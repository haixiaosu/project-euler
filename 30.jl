# A d-digit number x has a digit sum of 9^5*d.
# Likewise, by definition, x >= 10^(d-1).
# Thus, if `x` satisfies the digit fifth power condition,
# 10^(d-1) <= x <= 9^5*d.
# We conclude that d < 8.

function main()
  nums = Int64[]
  for x in 10:9999999
    digit_sum = 0
    y = x
    while y > 0
      digit_sum += (y % 10)^5
      y ÷= 10
    end
    if digit_sum == x
      push!(nums, x)
    end
  end
  println(sum(nums))
end

main()
