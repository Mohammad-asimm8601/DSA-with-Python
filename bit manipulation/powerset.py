def printAllSubsets(nums):
    n = len(nums)
    for i in range(2**n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(nums[j])
        print(temp, end=" ")

nums = [1, 2, 3]
printAllSubsets(nums)