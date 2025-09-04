def subarraySum():
        nums = [1,2,3]
        k = 3
        hashmap = {}
        prefix_sum = 0
        count = 0

        for right in range(len(nums)):
            prefix_sum += nums[right]
            if prefix_sum - k in hashmap:
                count += hashmap[prefix_sum - k]

            hashmap[prefix_sum] = hashmap.get(prefix_sum,0) + 1
        return count

result = subarraySum()
print(result)

# def checkSubarraySum():
#     nums = [1,3,6,0,9,6,9]
#     k = 7
#     prefix_sum = nums[0]

#     for i in range(1,len(nums)):
#         print((nums[i-1] + nums[i]) % k)
#         if (nums[i-1] + nums[i]) %  k == 0:
#             return True
#         prefix_sum += nums[i]
#         if prefix_sum % k == 0:
#             # print("Finally hogaya",prefix_sum)
#             return True
#     return False

# result = checkSubarraySum()
# print(result)