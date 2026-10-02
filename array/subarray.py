def maxSubArray(nums):
    n = len(nums)
    i = 0

    max_sum = float("-inf")
    sum = 0
    while i < n:
        sum += nums[i]
        sum = max(sum, nums[i])
        max_sum = max(max_sum, sum)
        i +=1
    
    return max_sum

nums = [-2, 1, 7, -3, 4, -1, 2, 1, -5, 4, 8]
result = maxSubArray(nums)
print(result)