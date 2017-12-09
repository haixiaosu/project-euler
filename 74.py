def fact(n):
    prod = 1
    for i in range(2, n + 1):
        prod *= i
    return prod
    
def calc(n):
    digit_sum = 0
    while n != 0:
        digit = n % 10
        digit_sum += digit
        
val = [-1] * 3000000
for num in range(1000000):
    