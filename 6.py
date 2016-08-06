num = 100
print(sum(i * j for i in range(num + 1) for j in range(num + 1) if i != j))