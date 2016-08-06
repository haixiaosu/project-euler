num = 600851475143
fact = 1
while num > 1:
    for i in range(3,num+1):
        if num % i == 0:
            fact = max(fact, i)
            num //= i
            break
print(fact)
