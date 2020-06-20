import copy

def permute(arr, n):
    arr_copy = copy.copy(arr)
    num_perms = 1
    for i in range(1, len(arr)):
        num_perms *= i

    perm = []
    while True:
        perm.append(arr_copy[n // num_perms])
        del arr_copy[n // num_perms]
        n %= num_perms
        if len(perm) == len(arr):
            break
        num_perms //= len(arr) - len(perm)
    return perm


if __name__ == "__main__":
    print(permute(list(range(10)), 1000000 - 1))
