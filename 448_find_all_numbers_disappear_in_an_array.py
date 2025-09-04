# def findDisappearedNumbers():
#     dictionary = {}
#     nums = [4,3,2,7,8,2,3,1]

#     dictionary = {}
#     for i in range(1, len(nums) + 1):
#         dictionary[i] = 0
    
#     for num in nums:
#         if num in dictionary:
#             dictionary[num] = 1
    
#     return 

# findDisappearedNumbers()

# def findDisappearedNumbers():
#         nums = [1,1]
#         n = len(nums)
#         for i in range(n):
#             print("Bahar",nums[nums[i] - 1],nums[i],nums)
#             while nums[i] != nums[nums[i] - 1]:
#                 print("Andar Pehle",nums[nums[i] - 1], nums[i],nums)
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#                 print("Andar Baadmei",nums[nums[i] - 1],nums[i],nums)
        
#         for i in range(n):
#             print("Final",nums[i],i + 1)
#         return [i + 1 for i in range(n) if nums[i] != i + 1]
# result = findDisappearedNumbers()
# print(result)

def findDisappearedNumbers(nums):
    """
    Modifies nums in‑place to mark seen values.
    Returns a list of integers in [1 … n] that are missing.
    Extra space used: O(1)  (output list not counted).
    """
    n = len(nums)

    # Pass 1: mark every encountered value
    for val in nums:
        idx = abs(val) - 1
        print(idx)
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    
    print(nums)
    # Pass 2: collect indices whose value is still positive
    missing = []
    for i in range(n):
        if nums[i] > 0:             # never touched ⇒ missing number
            missing.append(i + 1)   # convert back to 1‑based value

    return missing

# Example
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))   # ➜ [5, 6]
