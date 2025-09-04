def search():
    nums = [8,9,10,1,2,3,4,5,6,7]
    target = 11
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[left] <= nums[middle]:
            if nums[left]  <= target < middle:
                right = middle - 1
            else:
                left = middle + 1
        elif nums[middle] <= nums[right]:
            if nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1

result = search()
print(result)