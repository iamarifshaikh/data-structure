def numberOfArithmeticSlices():
    nums = [1,2,3,4]
    left = 0
    difference = 0
    for right in range(1,len(nums)):
        if not difference:
            difference = nums[right + 1] - nums[right]
        else:
            if nums[right + 1] - nums[right] == difference:
                count += 1
        while right - left >= 2:
            pass

print(numberOfArithmeticSlices())