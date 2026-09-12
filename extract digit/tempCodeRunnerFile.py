
# Method -2
def frequencyOfNum(nums):
    hash_map = {}
    n = len(nums)
    for i in range(0, n):
        hash_map[nums[i]] = hash_map.get(nums[1], 0)+1
    return hash_map

list = [1, 2, 3, 4, 2, 1, 4, 23, 53, 1, 4, 2, 3, 2, 1]
result = frequencyOfNum(list)
print(result)