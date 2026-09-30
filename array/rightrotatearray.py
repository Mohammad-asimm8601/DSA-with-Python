# Method -1

def right_rotate_array1(arr, k):
    # Using slicing
    arr[:] =  arr[-k:] + arr[:-k]


# method -2
def reverse(arr, i, j):
    while(i<j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def right_rotate_array2(arr, k):
     n = len(arr)
     if n==0:
         return 
     k = k % n 
     reverse(arr, n-k, n-1)
     reverse(arr, 0, n-k-1)
     reverse(arr, 0, n-1)



# calling functions
nums = [5, -2, 3, 9, 0, 6, 10, 7]

# right_rotate_array1(nums, 2)
right_rotate_array2(nums, 2)
print(nums)