def rearrangeElementsBySign1(nums):
    pos = [num for num in nums if num >= 0]
    neg = [num for num in nums if num < 0]

    result = []
    for p,n in zip(pos,neg):
        result.append(p)
        result.append(n)

    return result

def rearrangeElementsBySign2(nums):
    n = len(nums)
    pos = 0
    neg = 1
    result = [0]*n

    for i in range(n):
        if nums[i] > 0:
            result[pos] = nums[i]
            pos += 2
        else:
            result[neg] = nums[i]
            neg += 2

    return result

nums = [5, 10, -3, -1, -10, 6]
result = rearrangeElementsBySign2(nums)
print(result)
