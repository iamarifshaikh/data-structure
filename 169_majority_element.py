def majorityElement():
    nums = [2,2,1,1,1,2,]
    candidates = count = 0

    for i in range(len(nums)):
        if count == 0:
            candidates = nums[i]
            count += 1
        elif nums[i] != candidates:
            count -= 1
        else: count += 1
    
    count_again = 0
    for i in range(len(nums)):
        if nums[i] == candidates:
            count_again += 1
        
        if count_again >= len(nums) // 2:
            return candidates 

majorityElement()