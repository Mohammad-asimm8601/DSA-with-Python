def ceilTheFloor(nums, target):
    n = len(nums)
    lo = 0
    hi = n-1
    floor = -1
    ceil = -1
    while(lo <= hi):
        mid = (lo + hi)//2

        if nums[mid] == target:
            return nums[mid], nums[mid]

        elif nums[mid] > target:
            ceil = nums[mid]
            hi = mid - 1
        else :
            floor = nums[mid]
            lo = mid + 1
    return floor, ceil

nums = [3, 4,4,4,8,9,9,10,12,12,14,15]
target = 2
floor, ceil = ceilTheFloor(nums, target)
print(floor, ceil) 