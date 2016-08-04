import pprint

n = 101
array = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    array[i][0] = 1
    for j in range(1,n):
    	if j <= i:
    	     array[i][j] = array[i][j-1] + array[i-j-1][j]
	else:		 
	     array[i][j] = array[i][i]

pp = pprint.PrettyPrinter(indent=4,width=100)
pp.pprint(array)
print array[n-1][n-1]