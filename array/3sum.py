# Method - 1
def sum3_1(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = ([nums[i], nums[j], nums[k]])
                    temp.sort()
                    result.add(tuple(temp))

    return [list(ans) for ans in result]

# Method - 2
def sum3_2(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        my_set = set()
        for j in range(i+1, n):
            k_ele = -(nums[i]+nums[j])
            if k_ele in my_set:
                temp = ([nums[i], nums[j], k_ele])
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])            
                
    return [list(ans) for ans in result]

# Method - 3
def threeSum(nums):
    n = len(nums)
    ans =[]
    nums.sort()
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1]:
            continue

        j = i+1
        k = n-1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j<k and nums[j] == nums[j-1]:
                    j += 1
                while j<k and nums[k] == nums[k+1]:
                    k -= 1
    return ans

nums = [-1, 0, 1, 2,-1, -4]
# result = sum3_1(nums)      #Brute force 
# result = sum3_2(nums)      # Better
result = threeSum(nums)      # optimize
print(result)