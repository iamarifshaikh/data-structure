def threeSumClosest():
    # nums = [-1,2,1,-4]
    # target = 1
    # nums = [0,0,0]
    # target = 1
    # nums = [0,1,2]
    # target = 3
    # nums = [0,1,2]
    # target = 0
    # nums = [1,1,1,1]
    # target = 0
    # nums = [10,20,30,40,50,60,70,80,90]
    # target = 1
    nums = [4,0,5,-5,3,3,0,-4,-5]
    target = -2
    closest_sum = float('inf')
    nums.sort()
    
    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            sum_of = nums[i] + nums[j] + nums[k]
            # difference = sum_of - target
            if abs(closest_sum - target) > abs(sum_of - target):
                closest_sum = sum_of

            if difference == target:
                return difference
            elif difference > target:
                k -= 1
            else:
                j += 1

    return closest_sum

result = threeSumClosest()
print(result)