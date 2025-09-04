def findDuplicates():
    nums = [4,3,2,7,8,2,3,1]
    result = []
    for i in range(len(nums)):
        idx = abs(nums[i])-1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
        else:
            result.append(abs(nums[i]))
    print(result)
findDuplicates()