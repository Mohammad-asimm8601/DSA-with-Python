def minInRotatedSortedArray(nums):
    n = len(nums)

    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= nums[hi]:
            lo = mid + 1
        else:
            hi = mid - 1

    return nums[mid]


nums = [7, 8, 1, 2, 3, 4, 5, 6]
result = minInRotatedSortedArray(nums)
print(result)
