def maxSum():
        nums = [1,1,0,1,1]
      
        nums = set(nums)
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            if num < 0:
                continue
            else:
                current_sum += num
                max_sum = max(max_sum,current_sum)
        return max_sum
result = maxSum()
print(result)