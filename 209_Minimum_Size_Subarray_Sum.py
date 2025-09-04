def minSubArrayLen():
    target = 7
    nums = [2,3,1,2,4,3]
    left = 0
    curr_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        curr_sum += nums[right]
        if curr_sum > target:
            while curr_sum >= target:
                curr_sum -= nums[left]
                left += 1

        if curr_sum == target:
            min_length = min(min_length,right - left + 1)
    
    return min_length if min_length > 0 else 0

result = minSubArrayLen()
print(result)