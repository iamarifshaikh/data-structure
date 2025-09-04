def combinationSum():
    candidates = [2,3,6,7]
    target = 7
    result = []

    def backtracking(start,path,target):
        if target == 0:
            result.append(path[:])
            print(result)
            return

        if target < 0:
            return
        
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            backtracking(i,path,target - candidates[i])
            path.pop()

    backtracking(0,[],target)

    return result

result = combinationSum()
print(result)