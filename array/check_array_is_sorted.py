def is_array_sorted(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
        
    return True


arr = [1, 2, 4, 10]
result = is_array_sorted(arr)
print(result)
