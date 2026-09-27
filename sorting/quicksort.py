def partition(nums, low, high):
    pivot = nums[low]
    i = low 
    j = high
    while i<j:
        while i <= high - 1 and nums[i] <= pivot:
            i +=1
        while j >= low + 1 and nums[j] > pivot:
            j -= 1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)                                                                   
        quick_sort(arr, pi+1 , high)
    return arr

arr = [10, 7, 8, 9, 1, 5]
print(quick_sort(arr, 0, len(arr)-1))

                                                               