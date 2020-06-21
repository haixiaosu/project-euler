def diag_sum(max_m):
    # Initial 1 in the center.
    score = 1
    up_right_val = 1
    # Upper right diag sum increases by 8(m-1) each time for each "wrapper".
    for m in range(2, max_m + 1):
        up_right_val += 8 * (m - 1)
        score += 4 * up_right_val - 12 * m + 12
    return score

if __name__ == "__main__":
    print(diag_sum(501))
