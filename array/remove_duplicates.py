def remove_duplicates(arr):
    n = len(arr)
    freq = {}

    for ele in arr:
        freq[ele] = freq.get(ele, 0) + 1

    i = 0
    for key in freq:
        arr[i] = key
        i+=1
        
    return arr

nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 10]
result = remove_duplicates(nums)
print(result)