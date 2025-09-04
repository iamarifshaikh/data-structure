def findPeakElement():
    nums = [6,5,4,3,2,3,2]
    # nums = [1,2,3,1]
    # nums = [1,2,1,3,5,6,4]
    # nums = [1]
    # nums = [1,2]
    left = 0 
    right = len(nums) - 1
    res = 0

    while left < right:
        middle = (left + right) // 2
        if nums[middle] > nums[middle + 1]:
            right = middle - 1
        elif nums[middle] < nums[middle + 1]:
            left = middle + 1
    return right

res = findPeakElement()
print(res)