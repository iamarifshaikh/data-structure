class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashtable = {}
        left = 0
        maximum = float('-inf')
        
        for right in range(len(nums)):
            if nums[right] not in hashtable:
                hashtable[nums[right]] = 1
                maximum = max(maximum,sum(nums[left:right+1]))
            else:
                hashtable[nums[right]] += 1
                
                while True:
                    hashtable[nums[left]] -= 1
                    if nums[left] == nums[right]:
                        if hashtable[nums[left]] == 0:
                            del hashtable[nums[left]]
                        left += 1
                        break
                    else:
                        if hashtable[nums[left]] == 0:
                            del hashtable[nums[left]]
                    left += 1
        return maximum