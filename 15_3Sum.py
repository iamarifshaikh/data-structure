def threeSum():
    nums = [-1,0,1,2,-1,-4]
    nums.sort()
    i = 0
    j = 1
    k = len(nums) - 1
    result = []
    
    while i < j < k:
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i],nums[j],nums[k]])
                print(i,nums[i], j,nums[j], k,nums[k])
                break
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
        i += 1
        j = i + 1
        while j < k and nums[j] == nums[j - 1]:
            j += 1
        k = len(nums) - 1
        
    return result        
    
result = threeSum()
print(result)