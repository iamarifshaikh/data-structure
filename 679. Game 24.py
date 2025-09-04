# def judgePoint24(nums):
#     if len(nums) == 1:
#         return abs(nums[0] - 24.0) < 1e-6
    
#     for i in range(len(nums)):
#         for j in range(i + 1,len(nums)):
#             a,b = nums[i],nums[j]

#             new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

#             for op in [a+b,a-b,b-a,a*b]:
#                 if judgePoint24(new_nums + [op]): 
#                     return True
            
#             if b != 0:
#                 if judgePoint24(new_nums + [a/b]): 
#                     return True
            
#             if a != 0:
#                 if judgePoint24(new_nums + [b/a]): 
#                     return True
                
#     return False

# result = judgePoint24([1,2,1,2])
# print(result)

n = 3
w = 5
dp = [[0 for i in range(w)]  for _ in range(n+1)]

print(dp)