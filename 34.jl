function is_fact_sum(x)
  y = x
  fact_sum = 0
  while y > 0
    fact_sum += factorial(y % 10)
    y ÷= 10
  end
  return x == fact_sum
end

function main()
  nums = [x for x in 10:9999999 if is_fact_sum(x)]
  println(sum(nums))
end


main()
