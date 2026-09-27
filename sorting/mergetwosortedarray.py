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

nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 3, 4, 5, 6, 7]
result = mergeTwoSortedArray(nums1, nums2)
print(result)