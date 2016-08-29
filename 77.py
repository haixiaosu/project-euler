import sys

def get_primes(n):
    curr = 2
    primes  = [True] * n
    while curr < n:
        for i in range(curr + 1, n):
            primes[i] &= i % curr != 0
        curr += 1
        while curr < n and not primes[curr]:
            curr += 1
    result = [i for i in range(2,n) if primes[i]]
    return result

n = 100
primes = get_primes(n)
array = [[0 for x in range(len(primes))] for y in range(n)]

for i in range(n):
    array[i][0] = i % 2
    for j in range(1,len(primes)):
    	if primes[j] < i + 1:
    	     array[i][j] = array[i][j-1] + array[i-primes[j]][j]
        elif primes[j] == i + 1:
            array[i][j] = array[i][j-1] + 1
	else:		 
	     array[i][j] = array[i][j-1]
        if array[i][j] >= 5000:
            print(i + 1)
            sys.exit(0)
