import sys

n = 10000

array = []

for i in range(n):
    array.append([0] * (i + 1))
    array[i][0] = 1
    if i % 1000 == 0:
        print i
    for j in range(1,i):
        if j < (i - j - 1):
            array[i][j] = array[i][j-1] + array[i-j-1][j]
        else:
            array[i][j] = array[i][j-1] + array[i-j-1][-1]
        array[i][j] %= 1000000
    if i > 0:
        array[i][i] = 1 + array[i][i-1]
    if array[i][i] % 1000000 == 0:
        print (i + 1, array[i][i])
        sys.exit(0)
