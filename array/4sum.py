# Brute force
def fourSum_1(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == 0:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        result.add(tuple(temp))

    return [list(ans) for ans in result]


# better
def fourSum_2(nums):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i + 1, n):
            my_set = set()
            for k in range(j + 1, n):
                l_ele = -(nums[i] + nums[j] + nums[k])
                if l_ele in my_set:
                    temp = [nums[i], nums[j], nums[k], l_ele]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[k])

    return [list(ans) for ans in result]


# optimize
def fourSum_3(nums):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                total_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if total_sum < 0:
                    k += 1
                elif total_sum > 0:
                    l -= 1
                else:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1

    return ans


nums = [1, 0, -1, 0, -2, 2, 5, 9]
result = fourSum_3(nums)
print(result)
