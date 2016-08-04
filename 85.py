TARGET = 2000000
triangular_numbers = [1]
while triangular_numbers[-1] < TARGET:
    triangular_numbers.append(triangular_numbers[-1] + len(triangular_numbers) + 1)
 
i, j = 0, len(triangular_numbers) - 1
closest_prod = triangular_numbers[i] * triangular_numbers[j]
closest_area = (i + 1) * (j + 1)
while i <= j:
    prod = triangular_numbers[i] * triangular_numbers[j]
    if abs(prod - TARGET) < abs(closest_prod - TARGET):
        closest_prod = prod
        closest_area = (i + 1) * (j + 1)
    if prod > TARGET:
        j -= 1
    elif prod < TARGET:
        i += 1
    else:
        break
print(closest_area)
