def searchInsertPosition(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    idx = n
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= target:
            idx = mid 
            high = mid - 1
        else:
            low = mid + 1

    return idx


nums = [1, 3, 4, 5, 8, 9, 14, 15, 19, 20, 21]
target = 16
result = searchInsertPosition(nums, target)
print(result)
