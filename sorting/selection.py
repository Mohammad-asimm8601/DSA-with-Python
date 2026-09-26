# Ascending order sort

def selectionSortAsc(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if  nums[min_idx] > nums[j]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

# descending order sort

def selectionSortDesc(nums):
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if  nums[min_idx] < nums[j]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


nums = [5, 7, 8, 4 ,1, 6, 9, 2]
ASC_result = selectionSortAsc(nums)
print(ASC_result)

DESC_result = selectionSortDesc(nums)
print(DESC_result)
