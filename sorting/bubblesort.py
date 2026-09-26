def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        if not swapped:
            break
    return nums


nums = [5, 7, 8, 4 ,1, 6, 9, 2]
result = bubbleSort(nums)
print(nums)