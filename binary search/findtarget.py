# Iterative
def binarySearch1(arr, target):
    n = len(arr)

    low = 0
    high = n-1
    while(low <= high):
        mid = low + (high - low)//2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Target not exist"

# Using Recursion
def binarySearch2(arr, low, high, target):
    if low>high:
        return "Target not exist"
    mid = (low + high)//2
    if arr[mid] == target:
        return arr[mid]
    elif arr[mid] < target:
        return binarySearch2(arr, mid+1, high, target)
    else:
        return binarySearch2(arr, low, mid-1, target)


arr = [2, 4, 6, 7, 9, 11, 18,19]
target = 18
# result = binarySearch1(arr, target)    # iterative
result = binarySearch2(arr, 0, len(arr)-1, target)    # recursive
print(result)