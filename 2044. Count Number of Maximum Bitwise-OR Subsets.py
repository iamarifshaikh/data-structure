def countMaxOrSubsets():
    nums = [3,2,1,5]
    max_bit = 0

    for i in range(len(nums)):
        max_bit |= nums[i]
        # print(max_bit)
countMaxOrSubsets()

print(3 | 5)
print(3 | 1 | 5)
print(3 | 2 | 5)
print(3 | 2 | 1 | 5)
print(2 | 5)
print(2 | 1 |5)

print(3 | 2)

print(0 | 2)
print(2 | 1)
print(1 | 0)