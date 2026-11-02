def generateSubSequence(nums, target):
    result = []
    def solve(idx, total, subset):
        if total == target:
            result.append(subset.copy())
            return
        if idx >= len(nums) or total > target:
           return
            
            
        subset.append(nums[idx])
        solve(idx+1, total+nums[idx], subset)
        subset.pop()
        solve(idx+1, total, subset)

    solve(0, 0, [])
    return result



nums = [5, 9, 3, 4, 1]
target  = 9
result = generateSubSequence(nums, target)
print(result)
