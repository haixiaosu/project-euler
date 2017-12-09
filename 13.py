chain_map = {}


def generate_chain(n):
    if n in chain_map:
        return chain_map[n] 
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + generate_chain(n / 2)
    elif n % 2 == 1:
        return 1 + generate_chain(3 * n + 1)


longest = 0
max_i = -1
for i in range(1, 1000000):
    chain = generate_chain(i)
    if not i in chain_map:
        chain_map[i] = chain
    if chain > longest:
        longest = chain
        max_i = i
        
print(max_i)
