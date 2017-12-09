import mymaths
import math

d = 12000
fraction_sum = 0
for denominator in range(4, d + 1):
    for numerator in range(math.ceil(denominator / 3), math.floor(denominator / 2) + 1):
        if mymaths.gcd(denominator, numerator) == 1:
            fraction_sum += 1
            
print(fraction_sum)