def subsets():
    result = []
    nums = [1,2,3]
    def backtracking(start,path):
        if start >= len(nums): 
            result.append(path[:])
            # print(result)
            return result 
        
        backtracking(start + 1,path)
        path.append(nums[start])
        backtracking(start + 1,path)      
        path.pop()

    backtracking(0,[])
    print(result)
subsets()