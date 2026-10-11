# Lower Bound
def lowerBound(arr, target):
    n = len(arr)

    low = 0
    high = n-1
    lb = n
    while(low <= high):
        mid = low + (high - low)//2

        if arr[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return lb

def upperBound(arr, target):
    n = len(arr)

    low = 0
    high = n-1
    ub = n
    while(low <= high):
        mid = low + (high - low)//2

        if arr[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ub

nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1
# result = lowerBound(nums, target)
result = upperBound(nums, target)
print(result)