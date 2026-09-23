def reverse(nums, left, right):
    if left >= right:
        return 
    nums[left], nums[right] = nums[right], nums[left]
    reverse(nums, left+1, right-1)


def reverseArray(nums, left, right):
    reverse(nums, left, right)
    return nums


nums = [1, 2, 3, 4, 5]
result = reverseArray(nums, 0, len(nums)-1)
print(result)