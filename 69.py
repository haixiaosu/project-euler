import mymaths

MAX = 1000000
totient = mymaths.generate_totient(MAX)
print(max((1.0*n/totient[n] , n)for n in range(2, MAX)))