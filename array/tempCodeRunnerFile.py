
def remove_duplicates2(arr):
    n = len(arr)
    i = 0
    k = 1
    j = n-1
    while i<j:
        if arr[i] == arr[k]:
            while arr[k] == arr[j]:
                j -= 1
            else:
                arr[k], arr[j] = arr[j], arr[k]
                j -=1
        else:
            i = k
            k +=1
    return j

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 10]
k = remove_duplicates2(nums)
print(nums[:k])