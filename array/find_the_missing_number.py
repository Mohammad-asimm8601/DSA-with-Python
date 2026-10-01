# Using list

def missingNumber1(nums, n):
    result = [-1]*(n+1)

    for num in nums:
        result[num] = num

    for i in range(len(result)):
        if result[i] == -1:
            return i
    return i + 1


# Using mathematical formula
def missingNumber2(nums, n):
    n_sum = n*(n+1)//2
    list_sum = 0
    for num in nums:
        list_sum += num
    return n_sum - list_sum

nums = [1 ,0, 3, 4]
n = 4
result = missingNumber2(nums, 4)
print(result)