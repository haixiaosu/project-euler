function main()
  pent(n) = n * (3n - 1) ÷ 2
  pent_nums = pent.(1:10000)
  pent_num_set = Set(pent_nums)
  works = []
  for i in 1:length(pent_nums)
    for j in (i+1):length(pent_nums)
      if !in(pent_nums[j] - pent_nums[i], pent_num_set)
        continue
      end

      if !in(pent_nums[i] + pent_nums[j], pent_num_set)
        continue
      end

      push!(works, (i, j))
    end
  end
  println(works)
end

main()
