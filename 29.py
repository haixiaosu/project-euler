from math import *

top = 100


dictionary = {}
result = []

for step1 in range(2, top + 1):
	for step2 in range(2, top + 1):
		if step1 not in dictionary:
			dictionary[step1] = [] 
		dictionary[step1].append(step2)
		result.append((step1, step2))

for key, values in dictionary.items():
	for i in range(2, int(top / key) + 1):
		for value in values:
			if value % i == 0:
				try:
					result.remove(((key ** i), value / i))
				except ValueError: 
					pass 

print result
print len(result)
