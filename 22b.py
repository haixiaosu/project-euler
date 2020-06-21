def main():
    with open("p022_names.txt", "r") as fp:
        data = fp.read().split(",")

    score = 0
    for i, name in enumerate(sorted(data)):
        # Remove quotes.
        name = name[1:-1]
        score += (i + 1) * sum(ord(c) - ord("A") + 1 for c in name)
    print(score)



if __name__ == "__main__":
    main()
