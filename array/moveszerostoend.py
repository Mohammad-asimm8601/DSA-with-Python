def move_zeros_to_end1(arr):
    n = len(arr)

    i = 0
    j = 0
    while j < n:
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1
        j += 1

    while  i < n:
        arr[i] = 0
        i += 1
    
# method - 2

def move_zeros_to_end2(arr):
    n = len(arr)
    if n == 1:
        return
    
    i = 0
    while i < n:
        if arr[i] == 0:
            break
        i +=1
    if i == n:
        return 
    j = i + 1

    while j < n:
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j +=1

# calling
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
move_zeros_to_end2(nums)
print(nums)
