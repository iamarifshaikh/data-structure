# def new21Game():
#         n = 10
#         k = 1
#         maxPts = 10
        
#         if k == 0 or n >= k + maxPts:
#             return 1.0
        
#         dp = [0.0] * (n + 1)
#         dp[0] = 1.0  
        
#         window_sum = dp[0]
#         for x in range(1, n + 1):
#             dp[x] = window_sum / maxPts
            
#             if x < k:
#                 window_sum += dp[x]
            
#             if x - maxPts >= 0 and x - maxPts < k:
#                 window_sum -= dp[x - maxPts]
        
#         return sum(dp[k:])

# new21Game()
# def myPow():
#         x = 2.0000
#         n = 10
#         def power(x, n):
#             if n == 0:
#                 return 1
#             half = power(x, n // 2)
#             print(half,n)
#             if n % 2 == 0:
#                 return half * half
#             else:
#                 return half * half * x
        
#         if n < 0:
#             return 1 / power(x, -n)
#         else:
#             return power(x, n)

# myPow()

# number = 13
# i = 2
# mask = 1 << i
# print(mask)
# print((number & mask) >> i)

# def numberOfWays():
#         n = 10
#         x = 2
#         MOD = 10**9 + 7
#         print(MOD)
#         dp = [[0] * (n + 1) for _ in range(n + 1)]
#         print("DP Array: ",dp)
#         dp[0][0] = 1
#         for i in range(1, n + 1):
#             val = i**x
#             for j in range(n + 1):
#                 dp[i][j] = dp[i - 1][j]
#                 print(dp[i][j])
#                 if j >= val:
#                     dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
#         return dp[n][n]

# numberOfWays()

# def product_queries():
#         n = 15
#         queries = [[0,1],[2,2],[0,3]]
        
#         powers_of_two = []
      
#         # Extract powers of 2 from n by finding the rightmost set bit continuously
#         while n:
#             # x is the largest power of 2 in n, given by the bitwise AND of n and its two's complement
#             x = n & -n
#             # Add x to the list
#             powers_of_two.append(x)

#             # Remove the largest power of 2 from n
#             n -= x
#             print(x,n,powers_of_two)
      
#         # Set modulo as per the problem statement to avoid large integer overflow
#         mod = 10**9 + 7
      
#         # Initialize an array to store the results of the queries
#         results = []
      
#         # Loop through each query, which is a pair of indices (l, r)
#         for l, r in queries:
#             # Start with a product result of 1 for each query
#             product_result = 1
          
#             # Multiply the values from powers_of_two[l] to powers_of_two[r]
#             # and take the modulo to prevent overflow
#             for power in powers_of_two[l : r + 1]:
#                 product_result = (product_result * power) % mod
          
#             # Append the product result to the results list
#             results.append(product_result)

#         # Return the final list of results for all queries
#         return results
# product_queries()
# # def apply_updates(arr, updates):
# #     n = len(arr)
# #     diff = [0] * (n + 1)

# #     for (l, r, val) in updates:
# #         diff[l] += val
# #         if r + 1 < n:
# #             diff[r + 1] -= val

# #     for i in range(1, n):
# #         diff[i] += diff[i - 1]

# #     for i in range(n):
# #         arr[i] += diff[i]

# #     return arr

# # arr = [2, 3, 4, 6, 8]
# # updates = [(0, 2, 2),(3, 4, 4)]

# # result = apply_updates(arr, updates)
# # print(result)

# n = 15
# print(n & -n)

# def knapsack():
#     values = [60,100,120]
#     weights = [1,2,3]
#     capacity = 5
#     n = len(values) 
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n+1)]

#     for i in range(1, n + 1):  
#         for w in range(1, capacity + 1):
#             if weights[i-1] <= w:
#                 dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
#             else:
#                 dp[i][w] = dp[i-1][w]

#     for row in dp:
#         print(row)
# knapsack()


# def countSquares():
#     grid = [
#         [0,1,1,1],
#         [1,1,1,1],
#         [0,1,1,1]
#     ]

#     n = len(grid)
#     m = len(grid[0])

    # dp = [[grid[j][i] if i  == 0 or j == 0 else 0 for i in range(m)]for j in range(n)]
    # dp = [[0] * m for i in range(n)]    
    # print(dp)
    
    # total = 0
    # for i in range(n):
    #     for j in range(m):
    #         if i == 0 or j == 0:
    #             dp[i][j] = grid[i][j]
    #         else:
    #             dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

    #         total += dp[i][j]
    
    # for i in range(1,n):
    #     for j in range(1,m):
    #         if grid[i][j] == 0:
    #             dp[i][j] = 0
    #         else:
    #             dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1 
    # total = 0

    # for i in range(n):
    #     for j in range(m):
    #         total += dp[i][j]

# countSquares()
# def numSubmat():
#     mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
#     row = len(mat)
#     col = len(mat[0])
#     ans = 0
#     grid = [[mat[r][c] for c in range(col)] for r in range(row)]
    
#     for r in range(row):
#         for c in range(col):
#             if r == 0:
#                 if c == 0:
#                     grid[r][c] = mat[r][c]
#                 elif mat[r][c] == 1:
#                     grid[r][c] = grid[r][c-1] + 1
#             elif r != 0 and c == 0:
#                 if mat[r][c] == 1:
#                     grid[r][c] = 1 + grid[r-1][c]
#             elif mat[r][c] != 0:
#                 grid[r][c] = max(grid[r-1][c],max(grid[r][c-1],grid[r-1][c-1]))
#     print(grid)
    # for r in range(row):
    #     for c in range(col):
    #         if r == 0 and c == 0:
    #             if grid[r][c] == 1:
    #                 ans += 1
    #         elif r == 0:
    #             if grid[r][c] != 0:
    #                 ans = ans + grid[r][c] + grid[r][c-1]
    #         elif c == 0:
    #             if grid[r][c] != 0:
    #                 ans = ans + grid[r-1][c] + grid[r][c]
    #         else:
    #             if 




# numSubmat()

# def search():
#         # nums = [7,1,2,3,4,5,6]
#         nums = [5,1,3]
#         target = 3
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             middle = (left + right) // 2
#             print("Left: ",left,"Middle: ",middle,"Right: ",right)
#             if nums[middle] == target:
#                 return middle
#             elif nums[left] <= nums[middle]:
#                 if nums[left] <= target < nums[middle]:
#                     right = middle - 1
#                 else: left = middle + 1
#             else:
#                 if nums[middle] < target <= nums[right]:
#                     left = middle + 1
#                 else: right = middle - 1 
#         return -1

# result = search()
# print(result)


# def minimumArea():
#     # grid = [
#     #     [0,1,0],
#     #     [1,0,1]
#     # ]

#     # grid = [[1,0],[0,0]]
#     grid = [[0],[1]]

#     row = len(grid)
#     col = len(grid[0])

#     minRow = float('inf')
#     maxRow = float('-inf')   
#     minCol = float('inf')
#     maxCol = float('-inf')

#     for r in range(row):
#         for c in range(col):
#             if grid[r][c] == 1:
#                 minRow = min(minRow,r)
#                 maxRow = max(maxRow,r)
#                 minCol = min(minCol,c)
#                 maxCol = max(maxCol,c)
    
#     return (maxRow - minRow + 1) * (maxCol - minCol + 1)

# print(minimumArea())

# print(11 % 10)

# print(5 // 10)

# from collections import deque

# q = deque([1,2,3,4,5,6])
# q.popleft()
# q.rotate(3)
# print(q)

# def addOperators():
#         s = "123"
#         target = 6
#         result = []
#         def backtrack(index,expression):
#             print(expression)
#             if index == len(s):
#                 total = eval(expression)
#                 if total == target:
#                     result.append(expression)
#                     print(result)
#                     return
                 
#             if index >= len(s):
#                 return
            
#             if index == len(s) - 1:
#                 backtrack(index + 1,expression + f"{s[index]}")
#                 backtrack(index + 1,expression + f"{s[index]}")
#             else:
#                 backtrack(index + 1,expression + f"{s[index]}+")
#                 backtrack(index + 1,expression + f"{s[index]}*")
                 

#         backtrack(0,"")
# addOperators()

# print((one+two+three+four)/4)
# def numberOfPairs():    
#     nums = [[1,1],[2,2],[3,3]]
#     nums.sort()
#     count = 0

#     for j in range(len(nums)):
#         row = nums[j][0]
#         col = nums[j][1]

#         for r in range(len(nums)):
#                 if nums[r][0] == row and nums[r][1] == col:
#                     print("Continue hoga")
#                     continue
#                 else:
#                     if nums[r][1] <= col and row >= nums[r][0]:
#                         print(nums[r])
#                         for i in range(len(nums)):
#                             if (nums[i][0] == row and nums[i][1] == col) or (nums[i][0] == nums[r][0] and nums[i][1] == nums[r][1]):
#                                 print("yeh hit hua",nums[i])
#                                 continue
#                             if col <= nums[i][1] <= nums[r][1] or nums[r][1] <= nums[i][1] <= col:
#                                 print("Mil gaya",nums[r],row,col)
#                                 continue
#                             else:
#                                 print(count,nums[i],nums[r])
#                                 count += 1
#     print(count)

# numberOfPairs()

# def setMatrixZero():
#     matrix = [
#         [0,1,2,0],
#         [3,4,5,2],
#         [1,3,1,5]
#         ]
    
#     row = len(matrix)
#     col = len(matrix[0])

#     firstRow = any(matrix[0][x] == 0 for x in range(col))
#     firstCol = any(matrix[x][0] == 0  for x in range(row))

#     for r in range(1,row):
#         for c in range(1,col):
#             if matrix[r][c] == 0: 
#                 matrix[0][c] = 0
#                 matrix[r][0] = 0
    
#     for r in range(1,row):
#         for c in range(1,col):
#             if matrix[r][c] != 0:
#                 if matrix[r][0] == 0 or matrix[0][c] == 0: 
#                     matrix[r][c] = 0

#     if firstRow:
#         for r in range(col):
#             matrix[0][r] = 0

#     if firstCol:
#         for c in range(row):
#             matrix[c][0] = 0

#     print(matrix)

# setMatrixZero()

# import math

# def replaceNonCoprimes():
#     nums = [287,41,49,287,899,23,23,20677,5,825]

#     print(math.gcd(287,41))
#     print(math.gcd(41,49))

#     stack = []
#     num = 0

#     while num < len(nums):
#         while stack and num < len(nums) and math.gcd(stack[-1],nums[num]) > 1:
#             popped = stack.pop()
#             print(popped,nums[num],math.gcd(popped,nums[num]),math.lcm(popped,nums[num]))
#             stack.append(math.lcm(popped,nums[num]))
#             num += 1
#         if num < len(nums):
#             stack.append(nums[num])
#         num += 1
#     return stack 

# print(replaceNonCoprimes())

import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.tasks = tasks

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks.append([userId,taskId,priority])

    def edit(self, taskId: int, newPriority: int) -> None:
        pass

    def rmv(self, taskId: int) -> None:
        pass

    def execTop(self) -> int:
        pass

task = TaskManager([])
task.add(1,101,10)