def ceilTheFloor(nums, target):
    n = len(nums)
    lo = 0
    hi = n-1
    floor = -1
    ceil = -1
    while(lo <= hi):
        mid = (lo + hi)//2

        if nums[mid] >= target:
            floor = nums[mid]
        