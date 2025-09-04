def generatePrefix(nums):
    length = len(nums)
    prefix = [0] * (length + 1)

    for i in range(len(nums)):
        prefix[i + 1] = nums[i] + prefix[i]

    return prefix

def querieSum(prefix,start,end):
    return prefix[end + 1] - prefix[start]

nums = [1, 2, 3, 4, 5]
queries = [(0, 2), (1, 3), (0, 4)]

prefix = generatePrefix(nums)

for start,end in queries:
    result = querieSum(prefix,start,end)
    print(result)