import mymaths
MAX = 10000000
totient = mymaths.generate_totient(MAX)
min_ratio = MAX
min_n = 0
for n, tot in enumerate(totient):
    if n < 2: continue
    if mymaths.is_permutation(n, tot):
        ratio = 1.0*n/tot
        if ratio < min_ratio:
            print((n,tot,min_ratio))
            min_ratio = ratio
            min_n = n
print(min_n)