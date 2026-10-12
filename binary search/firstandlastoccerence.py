def firstOccurrence(nums, target):
    n = len(nums)

    lo = 0
    hi = n-1
    first = -1

    while(lo <= hi):
        mid = (lo + hi)//2
        if nums[mid] >= target:
            first = mid 
            hi = mid -1
        else:
            lo = mid + 1

    return first

def lastOccurrence(nums, target):
    n = len(nums)

    lo = 0
    hi = n-1
    last = -1

    while(lo <= hi):
        mid = (lo + hi)//2
        if nums[mid] > target:
            last = mid 
            hi = mid -1
        else:
            lo = mid + 1

    return last

nums = [1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10]
target = 3
first = firstOccurrence(nums, target)
last = lastOccurrence(nums, target)
print(first, last-1)