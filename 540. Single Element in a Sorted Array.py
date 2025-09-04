def singleNonDuplicate() -> int:
        # nums = [1,1,2,2,3]
        # nums = [1,1,2,3,3,4,4,8,8]
        # nums = [3,3,7,7,10,11,11]
        nums = [1,1,2,3,3]
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            return nums[-1]
        
        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1] 


        while left < right:
            middle = (left + right) // 2
            if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle+1]:
                return nums[middle]
            
            elif (middle - left + 1) % 2 == 0:
                if nums[middle] == nums[middle - 1]: left = middle + 1
                else: right = middle  - 1
                     
            elif (middle - left + 1) % 2 != 0:
                if nums[middle] == nums[middle - 1]: right = middle - 1
                else: left = middle + 1
        return nums[left]

result = singleNonDuplicate()
print(result)