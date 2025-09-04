def majorityElement():
    # nums = [3,2,3]
    # nums = [5,6,6]
    nums = [4,2,1,1]
    candidate1,candidate2,count1,count2,result = None,None,0,0,[]

    if len(nums) == 1:
        return nums

    for i in range(len(nums)):
        if candidate1 == nums[i]:
            count1 += 1
        elif candidate2 == nums[i]:
            count2 += 1
        elif count1 == 0:
            candidate1 = nums[i]
            count1 += 1
        elif count2 == 0:
            candidate2 = nums[i]
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    count_again_1 = 0
    count_again_2 = 0

    for verify in range(len(nums)):
        if nums[verify] == candidate1:
            count_again_1 += 1
        elif nums[verify] == candidate2:
            count_again_2 += 1

    if count_again_1 > len(nums) // 3:
        result.append(candidate1) 
    if count_again_2 > len(nums) // 3:
        result.append(candidate2)
    return result

result = majorityElement()
print(result)