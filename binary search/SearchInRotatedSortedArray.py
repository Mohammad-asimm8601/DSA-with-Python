def searchInRotatedSortedArray(nums, target):
    n = len(nums)
    lo = 0
    hi = n-1
    while lo <= hi:
        mid = (lo+hi)//2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[hi]:
            if nums[mid] <= target <= nums[hi]:
                lo = mid+1
            else:
                hi = mid -1
        else:
            if nums[lo] <= target <= nums[mid]:
                hi = mid -1
            else:
                lo = mid + 1

    return -1

nums = [11 ,15, 20,1, 4, 5, 6, 8, 9, 10]
target = 1
result = searchInRotatedSortedArray(nums, target)
print(result)


    