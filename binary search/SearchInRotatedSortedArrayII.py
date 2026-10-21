def searchInRotatedSortedArray(nums, target):
    n = len(nums)
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True
        if nums[mid] < nums[hi]:
            if nums[mid] <= target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if nums[lo] <= target <= nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

    return False


nums = [7, 7, 7, 7, 7, 7, 7, 1, 2, 3, 4, 5, 7, 7]
target = 6
result = searchInRotatedSortedArray(nums, target)
print(result)
