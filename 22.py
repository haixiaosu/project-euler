names_file = open("p022_names.txt","r")
names = names_file.read().split(",")
names.sort()

def char_order(character):
	return ord(character) - ord('A') + 1

def sum_name(name):
	return sum(map(char_order, list(name.strip('"'))))

print sum(map(lambda x: (x[0]+1) * x[1], list(enumerate(map(sum_name, names)))))