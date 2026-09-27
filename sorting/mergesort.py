def mergeTwoSortedArray(nums1, nums2):
    result = []
    i, j = 0, 0
    m, n = len(nums1), len(nums2)

    while(i < m and j < n):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i +=1
        else:
            result.append(nums2[j])
            j += 1
    while(i < m):
        result.append(nums1[i])
        i+=1

    while(j < n):
        result.append(nums2[j])
        j+=1
    
    return result

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left_nums = nums[ : mid]
    right_nums = nums[mid : ]
    return mergeTwoSortedArray(mergeSort(left_nums), mergeSort(right_nums))

nums = [3, 1, 2, 4, 1, 5, 2, 6, 4]
result = mergeSort(nums)
print(result)