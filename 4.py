import mymaths

largest = -1
for x in range(1, 999):
    for y in range(1, 999):
        result = x * y
        if mymaths.is_palindrome(result) and result > largest:
            largest = result
            
print(largest)
