def printAllSubsets(nums):
    for i in range(len(nums)):
        
        for j in range(i):
            temp.append(nums[j])
            print(temp, end=" ")

nums = [1, 2, 3]
printAllSubsets(nums)