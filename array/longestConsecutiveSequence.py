def longestConsecutiveSequence(nums):
    n = len(nums)
    if n==0:
        return 0
    
    nums.sort()

    longest = 1
    count = 1
    for i in range(n - 1):
        if nums[i] == nums[i+1]:
            continue
        if nums[i + 1] - nums[i] == 1:
            count += 1
        else:
            count = 1
        longest = max(longest, count)
    return count

def longestConsecutiveSequence2(nums):
    n = len(nums)
    if n==0:
        return 0
    
    nums_set = set(nums)

    longest = 0

    for num in nums_set:
        if num-1 not in nums_set:
            x = num
            count = 1
            while(x+1 in nums_set):
                count += 1
                x += 1
            longest = max(longest, count)

    return longest

nums = [1, 99, 101, 98, 2, 4, 5, 3, 100, 1, 1, 102]
result = longestConsecutiveSequence2(nums)
print(result)
