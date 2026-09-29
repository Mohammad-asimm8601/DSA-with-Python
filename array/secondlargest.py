def secondLargestElement(arr):
    largest = arr[0]
    second_largest = arr[1]
    for ele in arr:
        if ele > largest:
            second_largest = largest
            largest = ele

        elif ele > second_largest and ele != largest:
            second_largest = ele
    return second_largest

arr = [10, 5, 8]
# arr = [2, 9, 13, -45, 8,25, 93, -1, 0, 73, 101, 56, 1]
result = secondLargestElement(arr)
print(result)