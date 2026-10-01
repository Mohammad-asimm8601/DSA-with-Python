def mergeWithoutDuplicates(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    i = 0
    j = 0

    result = []


    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            value = nums1[i]
            i += 1
        
        else:
            value = nums2[j]
            j += 1

        if  not result or result[-1] != value:
            result.append(value)

    while i < m:
        if  not result  or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < n:
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j]) 
        j += 1

    return result


nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 2, 3, 6, 7, 8, 9, 10]

result = mergeWithoutDuplicates(nums1, nums2)
print(result)
