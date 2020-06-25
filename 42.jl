function get_sum(s)
  return sum(Int(c) - Int('A') + 1 for c in s)
end

function main()
  words = split(open(f->read(f, String), "p042_words.txt", "r"), ",")
  # Strip quotes.
  words = [s[2:end-1] for s in words]
  word_sum = map(get_sum, words)

  triangle_nums = Set(n * (n + 1) ÷ 2 for n in 1:100)
  count = 0
  for s in word_sum
    if s in triangle_nums
      count += 1
    end
  end
  println(count)
end

main()
