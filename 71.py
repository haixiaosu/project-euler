import math
r = 1000000
min_n = 0
min_d = 1
for d in range(1, r + 1):
    n_floor = math.floor(3.0 * d / 7)
    n_ceil = math.ceil(3.0 * d / 7)
    curr_diff = 3 * d - 7 * n_floor
    if min_n * d < n_floor * min_d and curr_diff > 0:
        min_n = n_floor
        min_d = d
print(min_n)