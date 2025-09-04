def zeroFilledSubarray():
    nums = [0,0,0,2,0,0]
    # dictionary = {i + 1:0 for i in range(len(nums))}

    # zero = 0
    # for right in range(len(nums)):
    #     if nums[right] == 0:
    #         zero += 1
    #         new_zero = zero
    #         while new_zero != 0:
    #             dictionary[new_zero] += 1
    #             new_zero -= 1
    #     else: zero = 0

    # total_subarrays = 0

    # for value in dictionary.values():
    #     total_subarrays += value
    #     if value == 0:
    #         break
    # return total_subarrays
 
    # Using Mathematics

    # count = 0
    # zero = 0
    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         zero += 1
    #     else:
    #         if zero != 0:
    #             print(zero,i)
    #             count += zero * (zero + 1) / 2
    #             zero = 0
    
    # if zero == 0: return int(count)
    # else:
    #     count += zero * (zero + 1) / 2
    #     return int(count)

    # Accumulation

    answer = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1 
            answer += count
        else: count = 0

result = zeroFilledSubarray()
print(result)