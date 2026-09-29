# Method - 1
def remove_duplicates1(arr):
    freq = {}

    for ele in arr:
        freq[ele] = 0

    i = 0
    for key in freq:
        arr[i] = key
        i+=1

    return i

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 10]
k = remove_duplicates1(nums)
print(nums[:k])

# Method -2

def remove_duplicates2(arr):
    n = len(arr)
    if n == 1:
        return 1
    
    i = 0
    j = 1
    idx = 0

    while i < n:
        while j< n and arr[i] == arr[j]:
            j += 1

        arr[idx] = arr[i]
        i = j
        idx +=1

    return idx
 

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 10]
k = remove_duplicates2(nums)
print(nums[:k])

# method - 3

def remove_duplicates3(arr):
    n = len(arr)
    if n==1:
        return 1
    
    i = 0
    j = i+1
    while j<n:
        if  arr[i] != arr[j]:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
        j+=1
       
        
    return i+1
 

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 10]
k = remove_duplicates3(nums)
print(nums[:k])