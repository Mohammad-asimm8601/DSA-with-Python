# Brute force solution

def twoSum1(nums, target):
    n = len(nums)

    for i in range(n - 1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return "Two elements sum equal target not exists"

# optimal

def twoSum2(nums, target):
    n = len(nums)
    hash_dict = {}
    for i in range(n):
        rem = target - nums[i]
        if rem not in hash_dict:
            hash_dict[nums[i]] = i
        else:
            return [hash_dict[rem], i]
    

nums = [5, 9, 1, 2, 4, 15, 6, 3]
target = 8
result = twoSum2(nums, target)
print(result)


