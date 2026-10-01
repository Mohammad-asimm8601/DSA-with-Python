def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return "target not exist in nums"


nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]
Target = 100
result = linearSearch(nums, Target)
print(result)
