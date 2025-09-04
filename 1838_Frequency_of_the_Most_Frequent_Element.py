def maxFrequency():
        nums = [1,4,8,13]
        k = 5
        nums.sort()
        left = 0
        total = 0          # sum of elements in the current window
        best  = 1

        for right in range(len(nums)):
            total += nums[right]
            while (right - left + 1) * nums[right] - total > k:
                total -= nums[left]    # shrink from the left
                left  += 1

            best = max(best, right - left + 1)

        return best

maxFrequency( )