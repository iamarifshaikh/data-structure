from collections import Counter
def findLonely():
    nums = [1,3,5,3]
    count = Counter(nums)
    lonely = []
    print(count)

    for num in nums:
            if num - 1 in count or num + 1 in count or count[num] >= 2:
                print(num)
                continue
            else:
                lonely.append(num)
    return lonely

result = findLonely()
print(result)