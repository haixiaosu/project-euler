def main():
    MOD = 10000000000
    res = 0
    for i in range(1, 1001):
        res += pow(i, i, MOD)
        res %= MOD
    print(res)

if __name__ == "__main__":
    main()
