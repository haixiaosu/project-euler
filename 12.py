import mymaths

n = 1
i = 2
while(True):
    num_of_divisors = mymaths.get_num_divisors(n)
    #print(n)
    #print(num_of_divisors)
    if (num_of_divisors > 500):
        print(n)
        break
    n = n + i
    i = i + 1
