function digits(x, base)
  res = Int32[]
  while x > 0
    push!(res, x % base)
    x ÷= base
  end
  res
end

function is_palindrome_arr(arr)
  for i in 1:(length(arr)÷2)
    if arr[i] != arr[length(arr) - i + 1]
      return false
    end
  end
  return true
end



function main()
  f = (x, base) -> is_palindrome_arr(digits(x, base))
  println(sum(x for x = 1:999999 if f(x, 10) && f(x, 2)))
end

main()
