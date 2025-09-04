def countHillValley():
    nums = [57,57,57,57,57,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,85,85,85,86,86,86]
    hillValue = 0
    i = 1
    j = 2

    while j < len(nums):
        if nums[i-1] != nums[i]:
            while j < len(nums) -1 and nums[i] == nums[j]:
                j += 1
            print(i,j)
            if nums[i-1] < nums[i] > nums[j]:
                hillValue += 1
                i += 1
                j = i + 1
            elif nums[i-1] > nums[i] < nums[j]:
                hillValue += 1
                i += 1
                j = i + 1
            else:
                i += 1
                j = i + 1
        else:
            i += 1
            j = i + 1
    return hillValue

result = countHillValley()
print(result)