def countCompleteSubarrays():
    nums = [1,3,1,2,2]
    total = len(set(nums))
    dictionary = {}
    left = 0
    count = 0

    for right in range(len(nums)):
        if total == len(dictionary):
            count += len(nums) - right + 1
        while len(dictionary) >= total:
            dictionary[nums[left]] -= 1
            if dictionary[nums[left]] == 0:
                del dictionary[nums[left]]
            if len(dictionary) == total:
                count += 1
            left += 1
        dictionary[nums[right]] = dictionary.get(nums[right], 0) + 1
    return count + 1

result = countCompleteSubarrays()
print(result)