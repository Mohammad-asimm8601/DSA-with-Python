def LargestElementInArray(arr):
    max_value = arr[0]
    for ele in arr:
        if ele > max_value:
            max_value = ele
    return max_value

arr = [2, 9, 13, -45, 8,25, 93, -1, 0, 73, 101, 56]
result = LargestElementInArray(arr)
print(result)