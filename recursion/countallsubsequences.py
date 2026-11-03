def countAllSubsequences(nums, target):
    def solve(idx, total):
        if total == target:
            return 1
        if idx >= len(nums) or total > target:
           return 0
            
        
        pick = solve(idx+1, total+nums[idx])
        not_pick = solve(idx+1, total)
        return pick+not_pick
    
    return solve(0, 0)


nums = [5, 9, 3, 4, 1]
target  = 9
result = countAllSubsequences (nums, target)
print(result)
