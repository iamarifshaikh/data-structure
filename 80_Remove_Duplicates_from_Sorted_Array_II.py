def removeDuplicates():
    nums = [0,0,1,1,1,1,2,3,3]
    k = 0

    for i in range(len(nums)):
        if k < 2 or nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k += 1
    
    return k

result = removeDuplicates()
print(result)