nums = [3, 4, 5, 6, 4, 8, 9, 10, 7, 1]
n = len(nums)
i=0


while(i < n):
    j = 0
    if nums[i] > nums [i+1]:
        nums[i+1], nums[j-1] = nums[j-1], nums[j]
    else:
        i +=1
        j +=1