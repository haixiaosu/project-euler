steps = range(2, 1001, 2)
print steps
current_number = 1
sum = 1
for step in steps:
	for mini_step in range(1, 5):
		current_number += step
		print current_number
		sum += current_number

print sum